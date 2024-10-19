from mido import MidiFile

# 读取MIDI文件
print("欢迎使用星雨引擎谱面启动器！请注意此启动器只能将midi文件读取为Tap音符")
path = input("请输入MIDI文件路径：>>>")

mid = MidiFile(path)

# 定义事件列表
events = []

# 遍历MIDI文件中的所有消息
for track in mid.tracks:
    absolute_time = 0  # 绝对时间
    for msg in track:
        absolute_time += msg.time
        if msg.type == 'note_on' and msg.velocity > 0:
            # 计算时间（以ticks为单位）
            time = absolute_time
            # 计算位置（假设音符范围为0-127，映射到-1到1）
            position = (msg.note - 64) / 64
            # 速度固定为spd
            speed = 'spd'
            # 添加事件到列表
            events.append((time, position, speed))

# 将事件转换为Click事件
click_events = []
for event in events:
    time, position, speed = event
    click_events.append(f'Click({time}, {position:.2f}, {speed})')

# 打印Click事件
for click_event in click_events:
    print(click_event)

# 将Click事件写入txt文件
with open('output.txt', 'w') as f:
    for click_event in click_events:
        f.write(click_event + '\n')

print("您的谱面已被写入 output.txt")