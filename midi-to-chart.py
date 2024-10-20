from mido import MidiFile

# 读取MIDI文件
print("欢迎使用星雨引擎谱面启动器！请注意此启动器只能将midi文件读取为Tap音符")
path = input("请输入MIDI文件路径：>>>")
mid = MidiFile(path)

# 定义事件列表
events = []
tempo = 500000  # 默认速度（微秒每拍）

# 遍历MIDI文件中的所有消息
for track in mid.tracks:
    absolute_time = 0  # 绝对时间
    for msg in track:
        absolute_time += msg.time
        if msg.type == 'note_on' and msg.velocity > 0:
            # 计算时间（以秒为单位）
            time = absolute_time / mid.ticks_per_beat * 60 / tempo
            # 计算位置（假设音符范围为0-127，映射到-1到1）
            position = (msg.note - 64) / 64
            # 根据通道确定事件类型
            if msg.channel == 0:
                event_type = 'Click'
            elif msg.channel == 1:
                event_type = 'Drag'
            elif msg.channel == 2:
                event_type = 'Flick'
            elif msg.channel == 3:
                event_type = 'Hold'
            else:
                continue  # 忽略其他通道
            # 添加事件到列表
            events.append((event_type, time, position, 'spd'))

# 将事件转换为字符串格式
event_strings = []
for event in events:
    event_type, time, position, speed = event
    if event_type == 'Hold':
        duration = 8  # 假设Hold事件的持续时间为8秒
        event_strings.append(f'{event_type}({time:.2f}, {position:.2f}, {speed}, {duration})')
    else:
        event_strings.append(f'{event_type}({time:.2f}, {position:.2f}, {speed})')

# 将事件写入txt文件
with open('output.py', 'w') as f:
    for event_string in event_strings:
        f.write(event_string + '\n')

print("您的谱面已被写入到 output.py")
