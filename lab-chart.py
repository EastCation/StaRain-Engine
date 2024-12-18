from phigros import *

bpm = 160
spd = 0.8
print ("Welcome to Use StaRain-Engine Based Phigros Eulator!")

d_line = Line(0.5, 0.5, 0, 0)

Offset(0.1)
with Multiplier(30 / bpm):
    with Line(0.5, 0) as line5:
        for i in range(1, 12):
            line5.set(i * 2, y=1)
            line5.set(i * 2 + 1, y=0)
        line5.set(26, width=0)
    d_line.set(21, width=0)
    d_line.set(23, width=1)
    Offset(26)
    with d_line:
        Click(3.00, 0.19, spd)
        Click(3.14, 0.22, spd)
        Click(3.27, 0.19, spd)
        Click(3.55, 0.14, spd)
        Click(3.82, 0.11, spd)
        Click(4.09, 0.14, spd)
        Click(4.36, 0.11, spd)
        Flick(4.36, -0.22, spd)
        Click(4.64, 0.08, spd)
        Flick(4.64, -0.16, spd)
        Click(4.91, 0.03, spd)
        Flick(4.91, -0.11, spd)
        Flick(5.18, -0.08, spd)
        Flick(5.45, -0.05, spd)
        Flick(5.73, 0.00, spd)
        Click(6.00, 0.11, spd)
        Flick(6.00, -0.08, spd)
        Click(6.27, 0.14, spd)
        Flick(6.27, -0.05, spd)
        Click(6.55, 0.11, spd)
        Flick(6.55, -0.23, spd)
        Click(6.82, 0.08, spd)
        Flick(6.82, -0.19, spd)
        Click(7.09, 0.00, spd)
        Flick(7.09, -0.11, spd)
        Flick(7.36, -0.08, spd)
        Flick(7.64, -0.05, spd)
        Flick(7.91, 0.00, spd)
        Click(8.18, 0.11, spd)
        Flick(8.18, -0.08, spd)
        Click(8.45, 0.14, spd)
        Flick(8.45, -0.05, spd)
        Click(8.73, 0.11, spd)
        Flick(8.73, -0.22, spd)
        Click(9.00, 0.08, spd)
        Flick(9.00, -0.16, spd)
        Click(9.27, 0.03, spd)
        Flick(9.27, -0.11, spd)
        Flick(9.55, -0.05, spd)
        Click(9.82, 0.08, spd)
        Flick(9.82, -0.03, spd)
        Click(10.09, 0.11, spd)
        Flick(10.09, 0.03, spd)
        Flick(10.36, -0.05, spd)
        Click(10.64, 0.03, spd)
        Flick(10.64, -0.03, spd)
        Click(10.91, 0.14, spd)
        Flick(10.91, -0.11, spd)
        Flick(11.18, -0.19, spd)
        Flick(11.45, -0.11, spd)
        Flick(11.73, -0.08, spd)
        Flick(12.00, -0.05, spd)
        Flick(12.27, 0.00, spd)
        Click(12.55, -0.11, spd)
        Flick(12.55, -0.08, spd)
        Click(12.61, -0.08, spd)
        Click(12.68, -0.05, spd)
        Click(12.75, 0.00, spd)
        Click(12.82, 0.03, spd)
        Flick(12.82, -0.05, spd)
        Click(12.89, 0.08, spd)
        Click(12.95, 0.11, spd)
        Click(13.02, 0.14, spd)
        Click(13.09, 0.19, spd)
        Flick(13.09, -0.34, spd)
        Flick(13.36, -0.23, spd)
        Click(13.64, 0.14, spd)
        Flick(13.64, -0.16, spd)
        Flick(13.91, -0.11, spd)
        Click(14.18, 0.14, spd)
        Flick(14.18, -0.08, spd)
        Click(14.45, 0.03, spd)
        Flick(14.45, -0.16, spd)
        Click(14.73, 0.14, spd)
        Flick(14.73, -0.11, spd)
        Click(15.00, 0.11, spd)
        Flick(15.00, -0.08, spd)
        Click(15.27, 0.17, spd)
        Flick(15.27, -0.27, spd)
        Click(15.55, 0.03, spd)
        Flick(15.55, -0.08, spd)
        Click(15.82, 0.17, spd)
        Flick(15.82, -0.16, spd)
        Click(16.09, 0.03, spd)
        Flick(16.09, -0.11, spd)
        Click(16.36, 0.17, spd)
        Flick(16.36, -0.08, spd)
        Click(16.64, 0.03, spd)
        Flick(16.64, -0.05, spd)
        Click(16.91, 0.17, spd)
        Flick(16.91, -0.11, spd)
        Click(17.18, 0.03, spd)
        Flick(17.18, -0.08, spd)
        Flick(17.45, -0.38, spd)
        Click(17.73, 0.30, spd)
        Flick(17.73, -0.27, spd)
        Click(17.82, 0.33, spd)
        Click(17.91, 0.30, spd)
        Click(18.00, 0.27, spd)
        Flick(18.00, -0.19, spd)
        Click(18.09, 0.30, spd)
        Click(18.18, 0.27, spd)
        Click(18.27, 0.19, spd)
        Flick(18.27, -0.11, spd)
        Click(18.36, 0.22, spd)
        Click(18.45, 0.19, spd)
        Click(18.55, 0.14, spd)
        Flick(18.55, -0.08, spd)
        Click(18.64, 0.19, spd)
        Click(18.73, 0.14, spd)
        Click(18.82, 0.11, spd)
        Flick(18.82, 0.00, spd)
        Click(18.91, 0.14, spd)
        Click(19.00, 0.11, spd)
        Click(19.09, 0.08, spd)
        Flick(19.09, -0.11, spd)
        Click(19.18, 0.11, spd)
        Click(19.27, 0.08, spd)
        Click(19.36, 0.03, spd)
        Flick(19.36, -0.08, spd)
        Click(19.45, 0.08, spd)
        Click(19.55, 0.03, spd)
        Click(19.64, 0.00, spd)
        Flick(19.64, -0.12, spd)
        Click(21.00, 0.11, spd)
        Click(21.27, 0.08, spd)
        Click(21.55, 0.03, spd)
        Click(21.82, 0.08, spd)
        Flick(21.82, -0.30, spd)
        Flick(22.09, -0.19, spd)
        Click(22.36, 0.08, spd)
        Flick(22.36, -0.11, spd)
        Click(22.64, 0.03, spd)
        Flick(22.64, 0.00, spd)
        Click(22.91, 0.08, spd)
        Click(23.45, 0.08, spd)
        Click(23.73, 0.03, spd)
        Click(24.00, 0.08, spd)
        Flick(24.00, -0.30, spd)
        Click(24.27, 0.03, spd)
        Flick(24.27, -0.19, spd)
        Click(24.55, 0.00, spd)
        Flick(24.55, -0.08, spd)
        Flick(24.82, 0.00, spd)
        Click(25.36, 0.11, spd)
        Flick(25.36, -0.08, spd)
        Click(25.64, 0.08, spd)
        Flick(25.64, -0.11, spd)
        Click(25.91, 0.03, spd)
        Flick(25.91, -0.08, spd)
        Click(26.18, 0.08, spd)
        Flick(26.18, -0.34, spd)
        Flick(26.45, -0.19, spd)
        Click(26.73, 0.08, spd)
        Flick(26.73, -0.11, spd)
        Click(27.00, 0.03, spd)
        Flick(27.00, 0.00, spd)
        Click(27.27, 0.08, spd)
        Click(27.82, 0.08, spd)
        Click(28.09, 0.14, spd)
        Click(28.36, 0.11, spd)
        Flick(28.36, -0.19, spd)
        Click(28.64, 0.08, spd)
        Flick(28.64, -0.11, spd)
        Click(28.91, 0.08, spd)
        Flick(28.91, -0.08, spd)
        Flick(29.18, 0.00, spd)
        Click(29.73, 0.00, spd)
        Flick(29.73, -0.08, spd)
        Click(30.00, 0.03, spd)
        Flick(30.00, -0.11, spd)
        Click(30.27, 0.14, spd)
        Flick(30.27, -0.08, spd)
        Click(30.55, 0.14, spd)
        Flick(30.55, -0.22, spd)
        Flick(30.82, -0.11, spd)
        Click(31.09, 0.14, spd)
        Flick(31.09, -0.05, spd)
        Click(31.36, 0.11, spd)
        Flick(31.36, 0.00, spd)
        Click(31.64, 0.14, spd)
        Click(32.18, 0.14, spd)
        Click(32.45, 0.11, spd)
        Click(32.73, 0.14, spd)
        Flick(32.73, -0.22, spd)
        Click(33.00, 0.19, spd)
        Flick(33.00, -0.11, spd)
        Flick(33.27, -0.05, spd)
        Click(33.55, 0.14, spd)
        Flick(33.55, 0.00, spd)
        Click(34.09, 0.14, spd)
        Flick(34.09, -0.05, spd)
        Click(34.36, 0.14, spd)
        Flick(34.36, -0.08, spd)
        Click(34.64, 0.14, spd)
        Flick(34.64, -0.05, spd)
        Click(34.91, 0.11, spd)
        Flick(34.91, -0.27, spd)
        Click(35.18, 0.11, spd)
        Flick(35.18, -0.19, spd)
        Click(35.45, 0.11, spd)
        Flick(35.45, -0.08, spd)
        Click(35.73, 0.11, spd)
        Flick(35.73, 0.00, spd)
        Click(36.00, 0.11, spd)
        Click(36.55, 0.08, spd)
        Flick(36.55, -0.11, spd)
        Click(36.82, 0.14, spd)
        Flick(37.09, -0.19, spd)
        Flick(37.14, -0.12, spd)
        Flick(37.18, -0.08, spd)
        Flick(37.23, 0.00, spd)
        Click(37.36, 0.11, spd)
        Click(38.45, 0.11, spd)
        Click(38.73, 0.08, spd)
        Click(39.00, 0.03, spd)
        Click(39.27, 0.08, spd)
        Flick(39.27, -0.30, spd)
        Flick(39.55, -0.19, spd)
        Click(39.82, 0.08, spd)
        Flick(39.82, -0.11, spd)
        Click(40.09, 0.03, spd)
        Flick(40.09, 0.00, spd)
        Click(40.36, 0.08, spd)
        Click(40.91, 0.08, spd)
        Click(41.18, 0.03, spd)
        Click(41.45, 0.08, spd)
        Flick(41.45, -0.30, spd)
        Click(41.73, 0.03, spd)
        Flick(41.73, -0.19, spd)
        Click(42.00, 0.00, spd)
        Flick(42.00, -0.08, spd)
        Flick(42.27, 0.00, spd)
        Click(42.82, 0.00, spd)
        Flick(42.82, -0.08, spd)
        Click(43.09, 0.03, spd)
        Flick(43.09, -0.11, spd)
        Click(43.36, 0.14, spd)
        Flick(43.36, -0.08, spd)
        Click(43.64, 0.19, spd)
        Flick(43.64, -0.23, spd)
        Flick(43.91, -0.12, spd)
        Click(44.18, 0.19, spd)
        Flick(44.18, -0.05, spd)
        Click(44.45, 0.14, spd)
        Flick(44.45, 0.00, spd)
        Click(44.73, 0.19, spd)
        Click(45.27, 0.19, spd)
        Click(45.55, 0.14, spd)
        Click(45.82, 0.11, spd)
        Flick(45.82, -0.34, spd)
        Click(46.09, 0.08, spd)
        Flick(46.09, -0.23, spd)
        Click(46.36, 0.08, spd)
        Flick(46.36, -0.16, spd)
        Flick(46.64, -0.11, spd)
        Click(47.18, 0.11, spd)
        Flick(47.18, -0.05, spd)
        Click(47.45, 0.08, spd)
        Click(47.73, 0.11, spd)
        Click(48.00, 0.14, spd)
        Flick(48.00, -0.22, spd)
        Click(48.27, 0.11, spd)
        Flick(48.27, -0.11, spd)
        Click(48.55, 0.11, spd)
        Flick(48.55, -0.05, spd)
        Click(48.82, 0.08, spd)
        Flick(48.82, 0.00, spd)
        Click(49.09, 0.11, spd)
        Click(49.64, 0.08, spd)
        Flick(49.64, -0.03, spd)
        Click(49.91, 0.03, spd)
        Click(50.18, 0.11, spd)
        Flick(50.18, -0.27, spd)
        Click(50.45, 0.08, spd)
        Flick(50.45, -0.19, spd)
        Click(50.73, 0.08, spd)
        Flick(50.73, -0.12, spd)
        Click(51.00, 0.03, spd)
        Flick(51.00, -0.08, spd)
        Click(51.27, 0.08, spd)
        Click(51.82, 0.08, spd)
        Flick(51.82, 0.00, spd)
        Click(52.09, 0.08, spd)
        Flick(52.36, -0.30, spd)
        Flick(52.64, -0.19, spd)
        Flick(52.91, -0.11, spd)
        Flick(53.18, -0.08, spd)
        Click(54.55, 0.16, spd)
        Flick(54.55, -0.19, spd)
        Flick(54.82, -0.14, spd)
        Click(55.09, 0.14, spd)
        Flick(55.09, -0.05, spd)
        Flick(55.36, 0.00, spd)
        Click(55.64, 0.11, spd)
        Flick(55.64, -0.08, spd)
        Flick(55.91, -0.05, spd)
        Click(56.18, 0.08, spd)
        Flick(56.18, -0.08, spd)
        Flick(56.45, -0.05, spd)
        Click(56.73, 0.03, spd)
        Flick(56.73, -0.22, spd)
        Flick(57.00, -0.11, spd)
        Flick(57.27, -0.03, spd)
        Flick(57.55, 0.03, spd)
        Click(58.36, 0.11, spd)
        Click(58.50, 0.14, spd)
        Click(58.91, 0.11, spd)
        Flick(58.91, -0.38, spd)
        Flick(59.18, -0.08, spd)
        Flick(59.45, 0.00, spd)
        Flick(59.73, 0.06, spd)
        Click(60.55, 0.11, spd)
        Click(60.82, 0.14, spd)
        Click(61.09, 0.00, spd)
        Flick(61.09, -0.23, spd)
        Flick(61.36, -0.12, spd)
        Flick(61.64, -0.08, spd)
        Flick(61.91, 0.00, spd)
        Click(62.73, 0.11, spd)
        Click(63.27, 0.08, spd)
        Flick(63.27, -0.34, spd)
        Flick(63.55, -0.23, spd)
        Flick(63.82, -0.16, spd)
        Flick(64.09, -0.11, spd)
        Flick(64.64, -0.05, spd)
        Click(65.45, 0.11, spd)
        Flick(65.45, -0.27, spd)
        Click(65.73, 0.03, spd)
        Flick(65.73, -0.16, spd)
        Flick(66.00, -0.11, spd)
        Flick(66.27, -0.03, spd)
        Click(67.09, 0.08, spd)
        Click(67.64, 0.11, spd)
        Flick(67.64, -0.38, spd)
        Flick(67.91, -0.16, spd)
        Flick(68.18, -0.08, spd)
        Flick(68.45, -0.03, spd)
        Flick(69.82, -0.30, spd)
        Click(70.09, 0.00, spd)
        Flick(70.09, -0.19, spd)
        Click(70.36, 0.03, spd)
        Flick(70.36, -0.11, spd)
        Click(70.64, 0.08, spd)
        Flick(70.64, -0.08, spd)
        Click(70.91, 0.11, spd)
        Click(71.18, 0.08, spd)
        Click(71.45, 0.11, spd)
        Flick(71.45, -0.05, spd)
        Click(71.73, 0.14, spd)
        Click(72.00, 0.16, spd)
        Flick(72.00, -0.19, spd)
        Flick(72.27, -0.14, spd)
        Click(72.55, 0.14, spd)
        Flick(72.55, -0.05, spd)
        Flick(72.82, 0.00, spd)
        Click(73.09, 0.11, spd)
        Flick(73.09, -0.08, spd)
        Flick(73.36, -0.05, spd)
        Click(73.64, 0.08, spd)
        Flick(73.64, -0.08, spd)
        Flick(73.91, -0.05, spd)
        Click(74.18, 0.03, spd)
        Flick(74.18, -0.22, spd)
        Flick(74.45, -0.11, spd)
        Flick(74.73, -0.03, spd)
        Flick(75.00, 0.03, spd)
        Drag(75.82, 0.11, spd)
        Click(76.36, 0.11, spd)
        Flick(76.36, -0.38, spd)
        Flick(76.64, -0.08, spd)
        Flick(76.91, 0.00, spd)
        Flick(77.18, 0.06, spd)
        Click(78.00, 0.11, spd)
        Click(78.27, 0.14, spd)
        Click(78.55, 0.19, spd)
        Flick(78.55, -0.23, spd)
        Flick(78.82, -0.19, spd)
        Flick(79.09, -0.08, spd)
        Flick(79.36, 0.00, spd)
        Click(80.18, 0.22, spd)
        Click(80.73, 0.08, spd)
        Flick(80.73, -0.34, spd)
        Flick(81.00, -0.23, spd)
        Flick(81.27, -0.16, spd)
        Flick(81.55, -0.11, spd)
        Flick(82.09, -0.05, spd)
        Click(82.36, 0.11, spd)
        Click(82.64, 0.14, spd)
        Click(82.91, 0.19, spd)
        Flick(82.91, -0.27, spd)
        Flick(83.18, -0.16, spd)
        Click(83.45, 0.14, spd)
        Flick(83.45, -0.11, spd)
        Flick(83.73, -0.03, spd)
        Click(84.00, 0.11, spd)
        Click(84.55, 0.08, spd)
        Click(85.09, 0.11, spd)
        Flick(85.09, -0.38, spd)
        Flick(85.36, -0.16, spd)
        Flick(85.64, -0.08, spd)
        Flick(85.91, -0.03, spd)
        Click(86.73, 0.08, spd)
        Click(87.27, 0.08, spd)
        Flick(87.27, -0.30, spd)
        Flick(87.55, -0.19, spd)
        Flick(87.82, -0.05, spd)
        Flick(88.09, -0.08, spd)
        Flick(88.91, -0.05, spd)
        Click(89.45, 0.08, spd)
        Flick(89.45, -0.11, spd)
        Flick(89.48, -0.05, spd)
        Flick(89.50, 0.00, spd)
        Click(91.09, 0.14, spd)
        Click(91.36, 0.19, spd)
        Click(91.64, 0.22, spd)
        Flick(91.64, -0.34, spd)
        Flick(91.91, -0.16, spd)
        Flick(92.18, -0.11, spd)
        Flick(92.45, -0.08, spd)
        Flick(92.73, 0.00, spd)
        Flick(93.00, -0.11, spd)
        Click(93.27, 0.19, spd)
        Flick(93.27, -0.08, spd)
        Click(93.55, 0.14, spd)
        Flick(93.55, -0.05, spd)
        Click(93.82, 0.11, spd)
        Flick(93.82, -0.27, spd)
        Flick(94.09, -0.17, spd)
        Flick(94.36, -0.08, spd)
        Flick(94.64, -0.05, spd)
        Flick(94.91, 0.00, spd)
        Flick(95.18, -0.11, spd)
        Click(95.45, 0.08, spd)
        Flick(95.45, -0.08, spd)
        Click(95.73, 0.11, spd)
        Flick(95.73, -0.05, spd)
        Click(96.00, 0.19, spd)
        Flick(96.00, -0.23, spd)
        Flick(96.27, -0.19, spd)
        Flick(96.55, -0.11, spd)
        Flick(96.82, -0.08, spd)
        Flick(97.09, 0.00, spd)
        Flick(97.36, -0.11, spd)
        Click(97.64, 0.19, spd)
        Flick(97.64, -0.08, spd)
        Click(97.91, 0.11, spd)
        Flick(97.91, -0.05, spd)
        Click(98.18, 0.08, spd)
        Flick(98.18, -0.25, spd)
        Flick(98.45, -0.20, spd)
        Flick(98.73, -0.11, spd)
        Flick(99.00, -0.08, spd)
        Flick(99.27, -0.02, spd)
        Flick(99.55, -0.11, spd)
        Click(99.82, 0.08, spd)
        Flick(99.82, -0.05, spd)
        Click(100.09, 0.11, spd)
        Flick(100.09, -0.02, spd)
        Click(100.36, 0.14, spd)
        Flick(100.36, -0.23, spd)
        Flick(100.64, -0.16, spd)
        Click(100.91, 0.11, spd)
        Flick(100.91, -0.08, spd)
        Flick(101.18, -0.05, spd)
        Click(101.45, 0.08, spd)
        Flick(101.45, -0.03, spd)
        Click(101.73, 0.08, spd)
        Flick(101.73, -0.11, spd)
        Click(102.00, 0.03, spd)
        Flick(102.00, -0.05, spd)
        Flick(102.27, -0.03, spd)
        Click(102.55, 0.08, spd)
        Flick(102.55, -0.27, spd)
        Flick(102.82, -0.16, spd)
        Click(103.09, 0.11, spd)
        Flick(103.09, -0.08, spd)
        Flick(103.36, -0.05, spd)
        Click(103.64, 0.14, spd)
        Flick(103.64, -0.03, spd)
        Click(103.91, 0.08, spd)
        Flick(103.91, -0.11, spd)
        Click(104.18, 0.03, spd)
        Flick(104.18, -0.05, spd)
        Flick(104.45, -0.03, spd)
        Click(104.73, 0.00, spd)
        Flick(104.73, -0.19, spd)
        Flick(105.00, -0.08, spd)
        Flick(105.27, -0.19, spd)
        Flick(105.55, -0.08, spd)
        Flick(105.82, 0.00, spd)
        Flick(106.09, -0.11, spd)
        Click(106.36, 0.14, spd)
        Flick(106.36, -0.16, spd)
        Click(106.64, 0.19, spd)
        Flick(106.64, -0.11, spd)
        Click(106.91, 0.11, spd)
        Flick(106.91, -0.12, spd)
        Click(108.27, 0.11, spd)
        Click(108.55, 0.08, spd)
        Click(108.82, 0.03, spd)
        Click(109.09, 0.08, spd)
        Flick(109.09, -0.30, spd)
        Flick(109.36, -0.19, spd)
        Click(109.64, 0.08, spd)
        Flick(109.64, -0.11, spd)
        Click(109.91, 0.03, spd)
        Flick(109.91, 0.00, spd)
        Click(110.18, 0.08, spd)
        Click(110.73, 0.08, spd)
        Click(111.00, 0.03, spd)
        Click(111.27, 0.08, spd)
        Flick(111.27, -0.30, spd)
        Click(111.55, 0.03, spd)
        Flick(111.55, -0.19, spd)
        Click(111.82, 0.00, spd)
        Flick(111.82, -0.08, spd)
        Flick(112.09, 0.00, spd)
        Click(112.64, 0.11, spd)
        Flick(112.64, -0.08, spd)
        Click(112.91, 0.08, spd)
        Flick(112.91, -0.11, spd)
        Click(113.18, 0.03, spd)
        Flick(113.18, -0.08, spd)
        Click(113.45, 0.08, spd)
        Flick(113.45, -0.34, spd)
        Flick(113.73, -0.19, spd)
        Click(114.00, 0.08, spd)
        Flick(114.00, -0.11, spd)
        Click(114.27, 0.03, spd)
        Flick(114.27, 0.00, spd)
        Click(114.55, 0.08, spd)
        Click(115.09, 0.08, spd)
        Click(115.36, 0.14, spd)
        Click(115.64, 0.11, spd)
        Flick(115.64, -0.19, spd)
        Click(115.91, 0.08, spd)
        Flick(115.91, -0.11, spd)
        Click(116.18, 0.08, spd)
        Flick(116.18, -0.08, spd)
        Flick(116.45, 0.00, spd)
        Click(117.00, 0.00, spd)
        Flick(117.00, -0.08, spd)
        Click(117.27, 0.03, spd)
        Flick(117.27, -0.11, spd)
        Click(117.55, 0.14, spd)
        Flick(117.55, -0.08, spd)
        Click(117.82, 0.14, spd)
        Flick(117.82, -0.22, spd)
        Flick(118.09, -0.11, spd)
        Click(118.36, 0.14, spd)
        Flick(118.36, -0.05, spd)
        Click(118.64, 0.11, spd)
        Flick(118.64, 0.00, spd)
        Click(118.91, 0.14, spd)
        Click(119.45, 0.14, spd)
        Click(119.73, 0.11, spd)
        Click(120.00, 0.14, spd)
        Flick(120.00, -0.22, spd)
        Click(120.27, 0.19, spd)
        Flick(120.27, -0.11, spd)
        Flick(120.55, -0.05, spd)
        Click(120.82, 0.14, spd)
        Flick(120.82, 0.00, spd)
        Click(121.36, 0.14, spd)
        Flick(121.36, -0.05, spd)
        Click(121.64, 0.14, spd)
        Flick(121.64, -0.08, spd)
        Click(121.91, 0.14, spd)
        Flick(121.91, -0.05, spd)
        Click(122.18, 0.11, spd)
        Flick(122.18, -0.27, spd)
        Click(122.45, 0.11, spd)
        Flick(122.45, -0.19, spd)
        Click(122.73, 0.11, spd)
        Flick(122.73, -0.08, spd)
        Click(123.00, 0.11, spd)
        Flick(123.00, 0.00, spd)
        Click(123.27, 0.11, spd)
        Click(123.82, 0.08, spd)
        Flick(123.82, -0.11, spd)
        Click(124.09, 0.14, spd)
        Flick(124.36, -0.19, spd)
        Flick(124.41, -0.12, spd)
        Flick(124.45, -0.08, spd)
        Flick(124.50, 0.00, spd)
        Click(124.64, 0.11, spd)
        Click(125.73, 0.11, spd)
        Click(126.00, 0.08, spd)
        Click(126.27, 0.03, spd)
        Click(126.55, 0.08, spd)
        Flick(126.55, -0.30, spd)
        Flick(126.82, -0.19, spd)
        Click(127.09, 0.08, spd)
        Flick(127.09, -0.11, spd)
        Click(127.36, 0.03, spd)
        Flick(127.36, 0.00, spd)
        Click(127.64, 0.08, spd)
        Click(128.18, 0.08, spd)
        Click(128.45, 0.03, spd)
        Click(128.73, 0.08, spd)
        Flick(128.73, -0.30, spd)
        Click(129.00, 0.03, spd)
        Flick(129.00, -0.19, spd)
        Click(129.27, 0.00, spd)
        Flick(129.27, -0.08, spd)
        Flick(129.55, 0.00, spd)
        Click(130.09, 0.00, spd)
        Flick(130.09, -0.08, spd)
        Click(130.36, 0.03, spd)
        Flick(130.36, -0.11, spd)
        Click(130.64, 0.14, spd)
        Flick(130.64, -0.08, spd)
        Click(130.91, 0.19, spd)
        Flick(130.91, -0.23, spd)
        Flick(131.18, -0.12, spd)
        Click(131.45, 0.19, spd)
        Flick(131.45, -0.05, spd)
        Click(131.73, 0.14, spd)
        Flick(131.73, 0.00, spd)
        Click(132.00, 0.19, spd)
        Click(132.55, 0.19, spd)
        Click(132.82, 0.14, spd)
        Click(133.09, 0.11, spd)
        Flick(133.09, -0.34, spd)
        Click(133.36, 0.08, spd)
        Flick(133.36, -0.23, spd)
        Click(133.64, 0.08, spd)
        Flick(133.64, -0.16, spd)
        Flick(133.91, -0.11, spd)
        Click(134.45, 0.11, spd)
        Flick(134.45, -0.05, spd)
        Click(134.73, 0.08, spd)
        Click(135.00, 0.11, spd)
        Click(135.27, 0.14, spd)
        Flick(135.27, -0.22, spd)
        Click(135.55, 0.11, spd)
        Flick(135.55, -0.11, spd)
        Click(135.82, 0.11, spd)
        Flick(135.82, -0.05, spd)
        Click(136.09, 0.08, spd)
        Flick(136.09, 0.00, spd)
        Click(136.36, 0.11, spd)
        Click(136.91, 0.08, spd)
        Flick(136.91, -0.03, spd)
        Click(137.18, 0.03, spd)
        Click(137.45, 0.11, spd)
        Flick(137.45, -0.27, spd)
        Click(137.73, 0.08, spd)
        Flick(137.73, -0.19, spd)
        Click(138.00, 0.08, spd)
        Flick(138.00, -0.12, spd)
        Click(138.27, 0.03, spd)
        Flick(138.27, -0.08, spd)
        Click(138.55, 0.08, spd)
        Click(139.09, 0.08, spd)
        Flick(139.09, 0.00, spd)
        Click(139.36, 0.08, spd)
        Flick(139.64, -0.30, spd)
        Flick(139.91, -0.19, spd)
        Flick(140.18, -0.11, spd)
        Flick(140.45, -0.08, spd)
        Click(141.82, 0.16, spd)
        Flick(141.82, -0.19, spd)
        Flick(142.09, -0.14, spd)
        Click(142.36, 0.14, spd)
        Flick(142.36, -0.05, spd)
        Flick(142.64, 0.00, spd)
        Click(142.91, 0.11, spd)
        Flick(142.91, -0.08, spd)
        Flick(143.18, -0.05, spd)
        Click(143.45, 0.08, spd)
        Flick(143.45, -0.08, spd)
        Flick(143.73, -0.05, spd)
        Click(144.00, 0.03, spd)
        Flick(144.00, -0.22, spd)
        Flick(144.27, -0.11, spd)
        Flick(144.55, -0.03, spd)
        Flick(144.82, 0.03, spd)
        Click(145.64, 0.11, spd)
        Click(145.77, 0.14, spd)
        Click(146.18, 0.11, spd)
        Flick(146.18, -0.38, spd)
        Flick(146.45, -0.08, spd)
        Flick(146.73, 0.00, spd)
        Flick(147.00, 0.06, spd)
        Click(147.82, 0.11, spd)
        Click(148.09, 0.14, spd)
        Click(148.36, 0.00, spd)
        Flick(148.36, -0.23, spd)
        Flick(148.64, -0.12, spd)
        Flick(148.91, -0.08, spd)
        Flick(149.18, 0.00, spd)
        Click(150.00, 0.11, spd)
        Click(150.55, 0.08, spd)
        Flick(150.55, -0.34, spd)
        Flick(150.82, -0.23, spd)
        Flick(151.09, -0.16, spd)
        Flick(151.36, -0.11, spd)
        Flick(151.91, -0.05, spd)
        Click(152.73, 0.11, spd)
        Flick(152.73, -0.27, spd)
        Click(153.00, 0.03, spd)
        Flick(153.00, -0.16, spd)
        Flick(153.27, -0.11, spd)
        Flick(153.55, -0.03, spd)
        Click(154.36, 0.08, spd)
        Click(154.91, 0.11, spd)
        Flick(154.91, -0.38, spd)
        Flick(155.18, -0.16, spd)
        Flick(155.45, -0.08, spd)
        Flick(155.73, -0.03, spd)
        Flick(157.09, -0.30, spd)
        Click(157.36, 0.00, spd)
        Flick(157.36, -0.19, spd)
        Click(157.64, 0.03, spd)
        Flick(157.64, -0.11, spd)
        Click(157.91, 0.08, spd)
        Flick(157.91, -0.08, spd)
        Click(158.18, 0.11, spd)
        Click(158.45, 0.08, spd)
        Click(158.73, 0.11, spd)
        Flick(158.73, -0.05, spd)
        Click(159.00, 0.14, spd)
        Click(159.27, 0.16, spd)
        Flick(159.27, -0.19, spd)
        Flick(159.55, -0.14, spd)
        Click(159.82, 0.14, spd)
        Flick(159.82, -0.05, spd)
        Flick(160.09, 0.00, spd)
        Click(160.36, 0.11, spd)
        Flick(160.36, -0.08, spd)
        Flick(160.64, -0.05, spd)
        Click(160.91, 0.08, spd)
        Flick(160.91, -0.08, spd)
        Flick(161.18, -0.05, spd)
        Click(161.45, 0.03, spd)
        Flick(161.45, -0.22, spd)
        Flick(161.73, -0.11, spd)
        Flick(162.00, -0.03, spd)
        Flick(162.27, 0.03, spd)
        Drag(163.09, 0.11, spd)
        Click(163.64, 0.11, spd)
        Flick(163.64, -0.38, spd)
        Flick(163.91, -0.08, spd)
        Flick(164.18, 0.00, spd)
        Flick(164.45, 0.06, spd)
        Click(165.27, 0.11, spd)
        Click(165.55, 0.14, spd)
        Click(165.82, 0.19, spd)
        Flick(165.82, -0.23, spd)
        Flick(166.09, -0.19, spd)
        Flick(166.36, -0.08, spd)
        Flick(166.64, 0.00, spd)
        Click(167.45, 0.22, spd)
        Click(168.00, 0.08, spd)
        Flick(168.00, -0.34, spd)
        Flick(168.27, -0.23, spd)
        Flick(168.55, -0.16, spd)
        Flick(168.82, -0.11, spd)
        Flick(169.36, -0.05, spd)
        Click(169.64, 0.11, spd)
        Click(169.91, 0.14, spd)
        Click(170.18, 0.19, spd)
        Flick(170.18, -0.27, spd)
        Flick(170.45, -0.16, spd)
        Click(170.73, 0.14, spd)
        Flick(170.73, -0.11, spd)
        Flick(171.00, -0.03, spd)
        Click(171.27, 0.11, spd)
        Click(171.82, 0.08, spd)
        Click(172.36, 0.11, spd)
        Flick(172.36, -0.38, spd)
        Flick(172.64, -0.16, spd)
        Flick(172.91, -0.08, spd)
        Flick(173.18, -0.03, spd)
        Click(174.00, 0.08, spd)
        Click(174.55, 0.08, spd)
        Flick(174.55, -0.30, spd)
        Flick(174.82, -0.19, spd)
        Flick(175.09, -0.11, spd)
        Flick(175.36, 0.00, spd)
        Click(176.73, -0.11, spd)
        Flick(176.73, -0.19, spd)
        Click(176.80, -0.08, spd)
        Click(176.86, -0.05, spd)
        Click(176.93, 0.00, spd)
        Click(177.00, 0.03, spd)
        Flick(177.00, -0.14, spd)
        Click(177.07, 0.08, spd)
        Click(177.14, 0.11, spd)
        Click(177.20, 0.14, spd)
        Click(177.27, 0.19, spd)
        Flick(177.27, -0.05, spd)
        Click(177.34, 0.14, spd)
        Click(177.41, 0.11, spd)
        Click(177.48, 0.08, spd)
        Click(177.55, 0.03, spd)
        Flick(177.55, 0.00, spd)
        Click(177.61, 0.00, spd)
        Click(177.68, -0.05, spd)
        Click(177.75, -0.08, spd)
        Click(177.82, -0.11, spd)
        Flick(177.82, -0.08, spd)
        Click(177.89, -0.08, spd)
        Click(177.95, -0.05, spd)
        Click(178.02, 0.00, spd)
        Click(178.09, 0.03, spd)
        Flick(178.09, -0.05, spd)
        Click(178.16, 0.08, spd)
        Click(178.23, 0.11, spd)
        Click(178.30, 0.14, spd)
        Click(178.36, 0.19, spd)
        Flick(178.36, -0.08, spd)
        Click(178.43, 0.14, spd)
        Click(178.50, 0.11, spd)
        Click(178.57, 0.08, spd)
        Click(178.64, 0.03, spd)
        Flick(178.64, -0.05, spd)
        Click(178.70, 0.00, spd)
        Click(178.77, -0.05, spd)
        Click(178.84, -0.08, spd)
        Click(178.91, 0.03, spd)
        Click(178.91, 0.14, spd)
        Flick(178.91, -0.22, spd)
        Flick(179.18, -0.11, spd)
        Flick(179.45, -0.03, spd)
        Flick(179.73, 0.03, spd)
        Click(180.00, 0.03, spd)
        Click(180.00, 0.14, spd)
        Click(181.09, 0.00, spd)
        Click(181.09, 0.11, spd)
        Flick(181.09, -0.38, spd)
        Flick(181.36, -0.08, spd)
        Flick(181.64, 0.00, spd)
        Flick(181.91, 0.06, spd)
        Click(182.18, 0.00, spd)
        Click(182.18, 0.11, spd)
        Click(183.27, -0.08, spd)
        Click(183.27, 0.06, spd)
        Flick(183.27, -0.23, spd)
        Flick(183.55, -0.12, spd)
        Flick(183.82, -0.08, spd)
        Flick(184.09, 0.00, spd)
        Click(184.36, -0.08, spd)
        Click(184.36, 0.06, spd)
        Flick(185.45, -0.34, spd)
        Click(185.73, 0.14, spd)
        Flick(185.73, -0.23, spd)
        Click(186.00, 0.11, spd)
        Flick(186.00, -0.16, spd)
        Click(186.27, 0.08, spd)
        Flick(186.27, -0.11, spd)
        Click(186.55, 0.03, spd)
        Click(186.82, 0.00, spd)
        Flick(186.82, -0.05, spd)
        Click(187.09, -0.08, spd)
        Click(187.36, -0.05, spd)
        Click(187.64, -0.11, spd)
        Click(187.64, 0.03, spd)
        Flick(187.64, -0.27, spd)
        Flick(187.91, -0.16, spd)
        Flick(188.18, -0.11, spd)
        Flick(188.45, -0.03, spd)
        Click(188.73, -0.11, spd)
        Click(188.73, 0.03, spd)
        Click(189.82, -0.08, spd)
        Click(189.82, 0.06, spd)
        Flick(189.82, -0.38, spd)
        Flick(190.09, -0.16, spd)
        Flick(190.36, -0.08, spd)
        Flick(190.64, -0.03, spd)
        Click(190.91, -0.08, spd)
        Click(190.91, 0.06, spd)
        Click(192.00, -0.03, spd)
        Click(192.00, 0.08, spd)
        Flick(192.00, -0.30, spd)
        Flick(192.27, -0.19, spd)
        Flick(192.55, -0.11, spd)
        Flick(192.82, -0.08, spd)
        Click(193.09, -0.03, spd)
        Click(193.09, 0.08, spd)
        Flick(193.64, -0.05, spd)
        Click(194.18, 0.16, spd)
        Flick(194.18, -0.19, spd)
        Flick(194.45, -0.14, spd)
        Click(194.73, 0.14, spd)
        Flick(194.73, -0.05, spd)
        Flick(195.00, 0.00, spd)
        Click(195.27, 0.11, spd)
        Flick(195.27, -0.08, spd)
        Flick(195.55, -0.05, spd)
        Click(195.82, 0.08, spd)
        Flick(195.82, -0.08, spd)
        Flick(196.09, -0.05, spd)
        Click(196.36, 0.03, spd)
        Click(196.36, 0.14, spd)
        Flick(196.36, -0.22, spd)
        Flick(196.64, -0.11, spd)
        Flick(196.91, -0.03, spd)
        Flick(197.18, 0.03, spd)
        Click(197.45, 0.03, spd)
        Click(197.45, 0.14, spd)
        Click(198.55, 0.00, spd)
        Click(198.55, 0.11, spd)
        Flick(198.55, -0.38, spd)
        Flick(198.82, -0.08, spd)
        Flick(199.09, 0.00, spd)
        Flick(199.36, 0.06, spd)
        Click(199.64, 0.00, spd)
        Click(199.64, 0.11, spd)
        Click(200.73, -0.08, spd)
        Click(200.73, 0.06, spd)
        Flick(200.73, -0.23, spd)
        Flick(201.00, -0.19, spd)
        Flick(201.27, -0.08, spd)
        Flick(201.55, 0.00, spd)
        Click(201.82, -0.08, spd)
        Click(201.82, 0.06, spd)
        Flick(202.91, -0.34, spd)
        Click(203.18, 0.14, spd)
        Flick(203.18, -0.23, spd)
        Click(203.45, 0.11, spd)
        Flick(203.45, -0.16, spd)
        Click(203.73, 0.08, spd)
        Flick(203.73, -0.11, spd)
        Click(204.00, 0.03, spd)
        Click(204.27, 0.00, spd)
        Flick(204.27, -0.05, spd)
        Click(204.55, -0.08, spd)
        Click(204.82, -0.05, spd)
        Click(205.09, -0.11, spd)
        Click(205.09, 0.03, spd)
        Flick(205.09, -0.27, spd)
        Flick(205.36, -0.16, spd)
        Flick(205.64, -0.11, spd)
        Flick(205.91, -0.03, spd)
        Click(206.18, -0.11, spd)
        Click(206.18, 0.03, spd)
        Click(207.27, -0.08, spd)
        Click(207.27, 0.06, spd)
        Flick(207.27, -0.38, spd)
        Flick(207.55, -0.16, spd)
        Flick(207.82, -0.08, spd)
        Flick(208.09, -0.03, spd)
        Click(208.36, -0.08, spd)
        Click(208.36, 0.06, spd)
        Click(209.45, 0.11, spd)
        Flick(209.45, -0.30, spd)
        Click(209.73, 0.14, spd)
        Flick(209.73, -0.19, spd)
        Click(210.00, 0.11, spd)
        Flick(210.00, -0.11, spd)
        Click(210.27, 0.14, spd)
        Flick(210.27, -0.08, spd)
        Click(210.55, 0.19, spd)
        Click(210.82, 0.14, spd)
        Click(211.09, 0.19, spd)
        Click(211.36, 0.14, spd)
        Click(211.64, 0.11, spd)
        Flick(211.64, -0.08, spd)
        Flick(211.91, -0.19, spd)
        Click(212.18, 0.11, spd)
        Flick(212.18, -0.11, spd)
        Click(212.45, 0.14, spd)
        Flick(212.45, -0.08, spd)
        Click(212.73, 0.03, spd)
        Click(213.27, 0.00, spd)
        Click(213.82, 0.11, spd)
        Flick(213.82, -0.03, spd)
        Click(214.09, 0.14, spd)
        Flick(214.09, -0.11, spd)
        Click(214.36, 0.11, spd)
        Flick(214.36, -0.03, spd)
        Click(214.64, 0.14, spd)
        Flick(214.64, 0.00, spd)
        Click(214.91, 0.19, spd)
        Click(215.18, 0.14, spd)
        Click(215.45, 0.19, spd)
        Click(215.73, 0.14, spd)
        Click(216.00, 0.11, spd)
        Flick(216.00, 0.00, spd)
        Flick(216.27, -0.11, spd)
        Click(216.55, 0.11, spd)
        Flick(216.55, -0.03, spd)
        Click(216.82, 0.14, spd)
        Flick(216.82, 0.00, spd)
        Click(217.09, 0.03, spd)
        Click(217.64, 0.00, spd)
        Click(218.18, 0.11, spd)
        Flick(218.18, -0.30, spd)
        Click(218.45, 0.14, spd)
        Flick(218.45, -0.19, spd)
        Click(218.73, 0.11, spd)
        Flick(218.73, -0.11, spd)
        Click(219.00, 0.14, spd)
        Flick(219.00, -0.05, spd)
        Click(219.27, 0.19, spd)
        Click(219.55, 0.14, spd)
        Click(219.82, 0.19, spd)
        Click(220.09, 0.14, spd)
        Click(220.36, 0.11, spd)
        Flick(220.36, -0.05, spd)
        Flick(220.64, -0.19, spd)
        Click(220.91, 0.11, spd)
        Flick(220.91, -0.11, spd)
        Click(221.18, 0.14, spd)
        Flick(221.18, -0.05, spd)
        Click(221.45, 0.03, spd)
        Click(222.00, 0.00, spd)
        Click(222.55, 0.11, spd)
        Flick(222.55, -0.03, spd)
        Click(222.82, 0.14, spd)
        Flick(222.82, -0.11, spd)
        Click(223.09, 0.11, spd)
        Flick(223.09, -0.03, spd)
        Click(223.36, 0.14, spd)
        Flick(223.36, 0.00, spd)
        Click(223.64, 0.19, spd)
        Click(223.91, 0.14, spd)
        Click(224.18, 0.19, spd)
        Click(224.45, 0.14, spd)
        Click(224.73, 0.11, spd)
        Offset(114)
preview()