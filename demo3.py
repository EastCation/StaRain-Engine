from phigros import *

bpm = 59
spd = 1.0

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
        Click(3.04, 0.22, spd)
        Click(3.42, 0.27, spd)
        Click(3.80, 0.22, spd)
        Click(4.18, 0.19, spd)
        Click(4.56, 0.22, spd)
        Click(4.94, 0.19, spd)
        Click(5.32, 0.22, spd)
        Click(6.08, 0.22, spd)
        Click(6.46, 0.19, spd)
        Click(6.84, 0.11, spd)
        Click(7.22, 0.16, spd)
        Click(7.59, 0.22, spd)
        Click(7.97, 0.19, spd)
        Click(9.11, 0.19, spd)
        Click(9.49, 0.16, spd)
        Click(9.87, 0.11, spd)
        Click(10.25, 0.16, spd)
        Click(10.63, 0.19, spd)
        Click(11.01, 0.22, spd)
        Click(11.39, 0.27, spd)
        Click(11.77, 0.19, spd)
        Click(12.15, 0.22, spd)
        Click(12.53, 0.27, spd)
        Click(12.91, 0.27, spd)
        Click(13.29, 0.11, spd)
        Click(13.67, 0.19, spd)
        Click(14.05, 0.16, spd)
        Click(15.19, 0.22, spd)
        Click(15.57, 0.27, spd)
        Click(15.95, 0.22, spd)
        Click(16.33, 0.19, spd)
        Click(16.71, 0.22, spd)
        Click(17.09, 0.19, spd)
        Click(17.47, 0.22, spd)
        Click(18.23, 0.22, spd)
        Click(18.61, 0.19, spd)
        Click(18.99, 0.11, spd)
        Click(19.37, 0.16, spd)
        Click(19.75, 0.22, spd)
        Click(20.13, 0.19, spd)
        Click(21.27, 0.19, spd)
        Click(21.65, 0.16, spd)
        Click(22.03, 0.11, spd)
        Click(22.41, 0.16, spd)
        Click(22.78, 0.19, spd)
        Click(23.16, 0.22, spd)
        Click(23.54, 0.27, spd)
        Click(23.92, 0.19, spd)
        Click(24.30, 0.22, spd)
        Click(24.68, 0.27, spd)
        Click(25.06, 0.27, spd)
        Click(25.44, 0.11, spd)
        Click(25.82, 0.19, spd)
        Click(26.20, 0.16, spd)
        Click(27.34, 0.19, spd)
        Click(27.72, 0.16, spd)
        Click(28.10, 0.11, spd)
        Click(28.50, 0.16, spd)
        Click(28.86, 0.19, spd)
        Click(29.25, 0.22, spd)
        Click(29.62, 0.27, spd)
        Click(30.01, 0.22, spd)
        Click(30.38, 0.22, spd)
        Click(30.76, 0.27, spd)
        Click(31.14, 0.27, spd)
        Click(31.52, 0.27, spd)
        Click(31.90, 0.22, spd)
        Click(33.42, 0.19, spd)
        Click(33.80, 0.19, spd)
        Click(34.18, 0.19, spd)
        Click(34.56, 0.16, spd)
        Click(34.94, 0.27, spd)
        Click(35.32, 0.27, spd)
        Click(35.70, 0.19, spd)
        Click(36.46, 0.08, spd)
        Click(36.84, 0.22, spd)
        Click(37.22, 0.22, spd)
        Click(37.97, 0.19, spd)
        Click(38.73, 0.22, spd)
        Click(39.49, 0.22, spd)
        Click(39.87, 0.27, spd)
        Click(40.25, 0.22, spd)
        Click(40.63, 0.19, spd)
        Click(41.01, 0.22, spd)
        Click(41.39, 0.19, spd)
        Click(41.77, 0.22, spd)
        Click(42.53, 0.22, spd)
        Click(42.91, 0.19, spd)
        Click(43.29, 0.11, spd)
        Click(43.67, 0.16, spd)
        Click(44.05, 0.22, spd)
        Click(44.43, 0.19, spd)
        Click(45.57, 0.19, spd)
        Click(45.95, 0.16, spd)
        Click(46.33, 0.11, spd)
        Click(46.71, 0.16, spd)
        Click(47.09, 0.19, spd)
        Click(47.47, 0.22, spd)
        Click(47.85, 0.27, spd)
        Click(48.23, 0.19, spd)
        Click(48.61, 0.22, spd)
        Click(48.99, 0.27, spd)
        Click(49.37, 0.27, spd)
        Click(49.75, 0.11, spd)
        Click(50.13, 0.19, spd)
        Click(50.51, 0.16, spd)
        Click(51.65, 0.19, spd)
        Click(52.03, 0.16, spd)
        Click(52.41, 0.11, spd)
        Click(52.78, 0.16, spd)
        Click(53.16, 0.19, spd)
        Click(53.54, 0.22, spd)
        Click(53.92, 0.27, spd)
        Click(54.30, 0.19, spd)
        Click(54.68, 0.22, spd)
        Click(55.06, 0.27, spd)
        Click(55.44, 0.27, spd)
        Click(55.82, 0.27, spd)
        Click(56.20, 0.22, spd)
        Click(57.72, 0.19, spd)
        Click(58.10, 0.19, spd)
        Click(58.48, 0.19, spd)
        Click(58.86, 0.16, spd)
        Click(59.24, 0.27, spd)
        Click(59.62, 0.27, spd)
        Click(60.00, 0.19, spd)
        Click(60.76, 0.08, spd)
        Click(61.14, 0.22, spd)
        Click(61.52, 0.19, spd)
        Click(61.90, 0.19, spd)
        Click(62.28, 0.16, spd)
        Click(65.32, 0.22, spd)
        Click(66.08, 0.27, spd)
        Click(66.84, 0.34, spd)
        Click(67.22, 0.27, spd)
        Click(67.59, 0.30, spd)
        Click(68.73, 0.30, spd)
        Click(69.11, 0.27, spd)
        Click(69.49, 0.22, spd)
        Click(69.87, 0.22, spd)
        Click(70.25, 0.27, spd)
        Click(70.63, 0.27, spd)
        Click(72.15, 0.22, spd)
        Click(72.53, 0.27, spd)
        Click(72.91, 0.30, spd)
        Click(73.29, 0.34, spd)
        Click(73.67, 0.38, spd)
        Click(74.05, 0.34, spd)
        Click(74.43, 0.30, spd)
        Click(74.81, 0.22, spd)
        Click(75.19, 0.19, spd)
        Click(75.57, 0.27, spd)
        Click(76.33, 0.22, spd)
        Click(78.23, 0.22, spd)
        Click(78.61, 0.27, spd)
        Click(78.99, 0.34, spd)
        Click(79.37, 0.27, spd)
        Click(79.75, 0.30, spd)
        Click(80.89, 0.34, spd)
        Click(81.27, 0.34, spd)
        Click(81.65, 0.34, spd)
        Click(82.03, 0.27, spd)
        Click(82.41, 0.22, spd)
        Click(82.78, 0.27, spd)
        Click(83.16, 0.34, spd)
        Click(83.54, 0.30, spd)
        Click(84.68, 0.22, spd)
        Click(85.06, 0.19, spd)
        Click(85.44, 0.22, spd)
        Click(85.82, 0.27, spd)
        Click(86.20, 0.41, spd)
        Click(86.58, 0.38, spd)
        Click(87.72, 0.34, spd)
        Click(88.10, 0.34, spd)
        Click(115.44, 0.22, spd)
        Click(115.82, 0.27, spd)
        Click(116.20, 0.22, spd)
        Click(116.58, 0.19, spd)
        Click(116.96, 0.22, spd)
        Click(117.34, 0.19, spd)
        Click(117.72, 0.22, spd)
        Click(118.48, 0.22, spd)
        Click(118.86, 0.19, spd)
        Click(119.24, 0.11, spd)
        Click(119.62, 0.16, spd)
        Click(120.00, 0.22, spd)
        Click(120.38, 0.19, spd)
        Click(121.52, 0.19, spd)
        Click(121.90, 0.16, spd)
        Click(122.28, 0.11, spd)
        Click(122.66, 0.16, spd)
        Click(123.04, 0.19, spd)
        Click(123.42, 0.22, spd)
        Click(123.80, 0.27, spd)
        Click(124.18, 0.19, spd)
        Click(124.56, 0.22, spd)
        Click(124.94, 0.27, spd)
        Click(125.32, 0.27, spd)
        Click(125.70, 0.11, spd)
        Click(126.08, 0.19, spd)
        Click(126.46, 0.16, spd)
        Click(127.59, 0.19, spd)
        Click(127.97, 0.16, spd)
        Click(128.35, 0.11, spd)
        Click(128.73, 0.16, spd)
        Click(129.11, 0.19, spd)
        Click(129.49, 0.22, spd)
        Click(129.87, 0.27, spd)
        Click(130.25, 0.19, spd)
        Click(130.63, 0.22, spd)
        Click(131.01, 0.27, spd)
        Click(131.39, 0.27, spd)
        Click(131.77, 0.27, spd)
        Click(132.15, 0.22, spd)
        Click(133.67, 0.19, spd)
        Click(134.05, 0.19, spd)
        Click(134.43, 0.19, spd)
        Click(134.81, 0.16, spd)
        Click(135.19, 0.27, spd)
        Click(135.57, 0.27, spd)
        Click(135.95, 0.19, spd)
        Click(136.71, 0.08, spd)
        Click(137.09, 0.22, spd)
        Click(137.47, 0.19, spd)
        Click(137.85, 0.19, spd)
        Click(138.23, 0.16, spd)
        Click(138.99, 0.22, spd)
        Click(139.37, 0.27, spd)
        Click(139.75, 0.34, spd)
        Click(140.13, 0.27, spd)
        Click(140.51, 0.30, spd)
        Click(141.65, 0.30, spd)
        Click(142.03, 0.27, spd)
        Click(142.41, 0.22, spd)
        Click(142.78, 0.22, spd)
        Click(143.16, 0.27, spd)
        Click(143.54, 0.27, spd)
        Click(145.06, 0.22, spd)
        Click(145.44, 0.27, spd)
        Click(145.82, 0.30, spd)
        Click(146.20, 0.34, spd)
        Click(146.58, 0.38, spd)
        Click(146.96, 0.34, spd)
        Click(147.34, 0.30, spd)
        Click(147.72, 0.22, spd)
        Click(148.10, 0.19, spd)
        Click(148.48, 0.27, spd)
        Click(149.24, 0.22, spd)
        Click(151.14, 0.22, spd)
        Click(151.52, 0.27, spd)
        Click(151.90, 0.34, spd)
        Click(152.28, 0.27, spd)
        Click(152.66, 0.30, spd)
        Click(153.80, 0.34, spd)
        Click(154.18, 0.34, spd)
        Click(154.56, 0.34, spd)
        Click(154.94, 0.27, spd)
        Click(155.32, 0.22, spd)
        Click(155.70, 0.27, spd)
        Click(156.08, 0.34, spd)
        Click(156.46, 0.30, spd)
        Click(157.60, 0.22, spd)
        Click(157.97, 0.19, spd)
        Click(158.35, 0.22, spd)
        Click(158.73, 0.27, spd)
        Click(159.11, 0.41, spd)
        Click(159.49, 0.38, spd)
        Click(160.63, 0.34, spd)
        Click(161.01, 0.34, spd)
        Click(163.29, 0.22, spd)
        Click(163.67, 0.27, spd)
        Click(164.05, 0.34, spd)
        Click(164.43, 0.27, spd)
        Click(164.81, 0.30, spd)
        Click(165.95, 0.30, spd)
        Click(166.33, 0.27, spd)
        Click(166.71, 0.22, spd)
        Click(167.09, 0.22, spd)
        Click(167.47, 0.27, spd)
        Click(167.85, 0.27, spd)
        Click(169.37, 0.22, spd)
        Click(169.75, 0.27, spd)
        Click(170.13, 0.30, spd)
        Click(170.51, 0.34, spd)
        Click(170.89, 0.38, spd)
        Click(171.27, 0.34, spd)
        Click(171.65, 0.30, spd)
        Click(172.03, 0.22, spd)
        Click(172.41, 0.19, spd)
        Click(172.78, 0.27, spd)
        Click(173.54, 0.22, spd)
        Click(175.44, 0.22, spd)
        Click(175.82, 0.27, spd)
        Click(176.20, 0.34, spd)
        Click(176.58, 0.27, spd)
        Click(176.96, 0.30, spd)
        Click(178.10, 0.34, spd)
        Click(178.48, 0.34, spd)
        Click(178.86, 0.34, spd)
        Click(179.24, 0.27, spd)
        Click(179.62, 0.22, spd)
        Click(180.00, 0.27, spd)
        Click(180.38, 0.34, spd)
        Click(180.76, 0.30, spd)
        Click(181.90, 0.22, spd)
        Click(182.28, 0.19, spd)
        Click(182.66, 0.22, spd)
        Click(183.04, 0.27, spd)
        Click(183.42, 0.41, spd)
        Click(183.80, 0.38, spd)
        Click(184.94, 0.34, spd)
        Click(185.32, 0.34, spd)
        Click(187.60, 0.22, spd)
        Click(187.97, 0.27, spd)
        Click(188.35, 0.34, spd)
        Click(188.73, 0.27, spd)
        Click(189.11, 0.30, spd)
        Click(190.25, 0.30, spd)
        Click(190.63, 0.27, spd)
        Click(191.01, 0.22, spd)
        Click(191.39, 0.22, spd)
        Click(191.77, 0.27, spd)
        Click(192.15, 0.27, spd)
        Click(193.67, 0.22, spd)
        Click(194.05, 0.27, spd)
        Click(194.43, 0.30, spd)
        Click(194.81, 0.34, spd)
        Click(195.19, 0.38, spd)
        Click(195.57, 0.34, spd)
        Click(195.95, 0.30, spd)
        Click(196.33, 0.22, spd)
        Click(196.71, 0.19, spd)
        Click(197.09, 0.27, spd)
        Click(197.85, 0.22, spd)
        Click(199.75, 0.22, spd)
        Click(200.13, 0.27, spd)
        Click(200.51, 0.34, spd)
        Click(200.89, 0.27, spd)
        Click(201.27, 0.30, spd)
        Click(202.41, 0.34, spd)
        Click(202.78, 0.34, spd)
        Click(203.16, 0.34, spd)
        Click(203.54, 0.27, spd)
        Click(203.92, 0.22, spd)
        Click(204.30, 0.27, spd)
        Click(204.68, 0.34, spd)
        Click(205.06, 0.30, spd)
        Click(206.20, 0.22, spd)
        Click(206.58, 0.19, spd)
        Click(206.96, 0.22, spd)
        Click(207.34, 0.27, spd)
        Click(207.72, 0.41, spd)
        Click(208.10, 0.38, spd)
        Click(209.24, 0.34, spd)
        Click(209.62, 0.34, spd)
        Click(218.73, 0.22, spd)
        Click(219.11, 0.27, spd)
        Click(219.49, 0.22, spd)
        Click(219.87, 0.19, spd)
        Click(220.25, 0.22, spd)
        Click(220.63, 0.19, spd)
        Click(221.01, 0.22, spd)
        Click(221.77, 0.22, spd)
        Click(222.15, 0.19, spd)
        Click(222.53, 0.11, spd)
        Click(222.91, 0.16, spd)
        Click(223.29, 0.22, spd)
        Click(223.67, 0.19, spd)
        Click(224.81, 0.19, spd)
        Click(225.19, 0.16, spd)
        Click(225.57, 0.11, spd)
        Click(225.95, 0.16, spd)
        Click(226.33, 0.19, spd)
        Click(226.71, 0.22, spd)
        Click(227.09, 0.27, spd)
        Click(227.47, 0.19, spd)
        Click(227.85, 0.22, spd)
        Click(228.23, 0.27, spd)
        Click(228.61, 0.27, spd)
        Click(228.99, 0.11, spd)
        Click(229.37, 0.19, spd)
        Click(229.75, 0.16, spd)
        Click(230.89, 0.19, spd)
        Click(231.27, 0.16, spd)
        Click(231.65, 0.11, spd)
        Click(232.03, 0.16, spd)
        Click(232.41, 0.19, spd)
        Click(232.78, 0.22, spd)
        Click(233.16, 0.27, spd)
        Click(233.54, 0.19, spd)
        Click(233.92, 0.22, spd)
        Click(234.30, 0.27, spd)
        Click(234.68, 0.27, spd)
        Click(235.06, 0.27, spd)
        Click(235.44, 0.22, spd)
        Click(236.96, 0.19, spd)
        Click(237.34, 0.19, spd)
        Click(237.72, 0.19, spd)
        Click(238.10, 0.16, spd)
        Click(238.48, 0.27, spd)
        Click(238.86, 0.27, spd)
        Click(239.24, 0.19, spd)
        Click(240.00, 0.08, spd)
        Click(240.38, 0.22, spd)
        Click(240.76, 0.19, spd)
        Click(241.14, 0.19, spd)
        Click(241.52, 0.16, spd)
        Click(242.28, 0.22, spd)
        Click(242.66, 0.27, spd)
        Click(243.04, 0.34, spd)
        Click(243.42, 0.27, spd)
        Click(243.80, 0.30, spd)
        Click(244.94, 0.30, spd)
        Click(245.32, 0.27, spd)
        Click(245.70, 0.22, spd)
        Click(246.08, 0.22, spd)
        Click(246.46, 0.27, spd)
        Click(246.84, 0.27, spd)
        Click(248.35, 0.22, spd)
        Click(248.73, 0.27, spd)
        Click(249.11, 0.30, spd)
        Click(249.49, 0.34, spd)
        Click(249.87, 0.38, spd)
        Click(250.25, 0.34, spd)
        Click(250.63, 0.30, spd)
        Click(251.01, 0.22, spd)
        Click(251.39, 0.19, spd)
        Click(251.77, 0.27, spd)
        Click(252.53, 0.22, spd)
        Click(254.43, 0.22, spd)
        Click(254.81, 0.27, spd)
        Click(255.19, 0.34, spd)
        Click(255.57, 0.27, spd)
        Click(255.95, 0.30, spd)
        Click(257.09, 0.34, spd)
        Click(257.47, 0.34, spd)
        Click(257.85, 0.34, spd)
        Click(258.23, 0.27, spd)
        Click(258.61, 0.22, spd)
        Click(258.99, 0.27, spd)
        Click(259.37, 0.34, spd)
        Click(259.75, 0.30, spd)
        Click(260.89, 0.22, spd)
        Click(261.27, 0.19, spd)
        Click(261.65, 0.22, spd)
        Click(262.03, 0.27, spd)
        Click(262.41, 0.41, spd)
        Click(262.78, 0.38, spd)
        Click(263.92, 0.34, spd)
        Click(264.30, 0.34, spd)
        Click(291.65, 0.22, spd)
        Click(292.03, 0.27, spd)
        Click(292.41, 0.22, spd)
        Click(292.78, 0.19, spd)
        Click(293.16, 0.22, spd)
        Click(293.54, 0.19, spd)
        Click(293.92, 0.22, spd)
        Click(294.68, 0.22, spd)
        Click(295.06, 0.19, spd)
        Click(295.44, 0.11, spd)
        Click(295.82, 0.16, spd)
        Click(296.20, 0.22, spd)
        Click(296.58, 0.19, spd)
        Click(297.72, 0.19, spd)
        Click(298.10, 0.16, spd)
        Click(298.48, 0.11, spd)
        Click(298.86, 0.16, spd)
        Click(299.24, 0.19, spd)
        Click(299.62, 0.22, spd)
        Click(300.00, 0.27, spd)
        Click(300.38, 0.19, spd)
        Click(300.76, 0.22, spd)
        Click(301.14, 0.27, spd)
        Click(301.52, 0.27, spd)
        Click(301.90, 0.11, spd)
        Click(302.28, 0.19, spd)
        Click(302.66, 0.16, spd)
        Click(303.80, 0.19, spd)
        Click(304.18, 0.16, spd)
        Click(304.56, 0.11, spd)
        Click(304.94, 0.16, spd)
        Click(305.32, 0.19, spd)
        Click(305.70, 0.22, spd)
        Click(306.08, 0.27, spd)
        Click(306.46, 0.19, spd)
        Click(306.84, 0.22, spd)
        Click(307.22, 0.27, spd)
        Click(307.60, 0.27, spd)
        Click(307.97, 0.27, spd)
        Click(308.35, 0.22, spd)
        Click(309.87, 0.19, spd)
        Click(310.25, 0.19, spd)
        Click(310.63, 0.19, spd)
        Click(311.01, 0.16, spd)
        Click(311.39, 0.27, spd)
        Click(311.77, 0.27, spd)
        Click(312.15, 0.19, spd)
        Click(312.91, 0.08, spd)
        Click(313.29, 0.22, spd)
        Click(313.67, 0.19, spd)
        Click(314.05, 0.19, spd)
        Click(314.43, 0.16, spd)
        Click(315.19, 0.22, spd)
        Click(315.57, 0.27, spd)
        Click(315.95, 0.34, spd)
        Click(316.33, 0.27, spd)
        Click(316.71, 0.30, spd)
        Click(317.85, 0.30, spd)
        Click(318.23, 0.27, spd)
        Click(318.61, 0.22, spd)
        Click(318.99, 0.22, spd)
        Click(319.37, 0.27, spd)
        Click(319.75, 0.27, spd)
        Click(321.27, 0.22, spd)
        Click(321.65, 0.27, spd)
        Click(322.03, 0.30, spd)
        Click(322.41, 0.34, spd)
        Click(322.78, 0.38, spd)
        Click(323.16, 0.34, spd)
        Click(323.54, 0.30, spd)
        Click(323.92, 0.22, spd)
        Click(324.30, 0.19, spd)
        Click(324.68, 0.27, spd)
        Click(325.44, 0.22, spd)
        Click(327.34, 0.22, spd)
        Click(327.72, 0.27, spd)
        Click(328.10, 0.34, spd)
        Click(328.48, 0.27, spd)
        Click(328.86, 0.30, spd)
        Click(330.00, 0.34, spd)
        Click(330.38, 0.34, spd)
        Click(330.76, 0.34, spd)
        Click(331.14, 0.27, spd)
        Click(331.52, 0.22, spd)
        Click(331.90, 0.27, spd)
        Click(332.28, 0.34, spd)
        Click(332.66, 0.30, spd)
        Click(333.80, 0.22, spd)
        Click(334.18, 0.19, spd)
        Click(334.56, 0.22, spd)
        Click(334.94, 0.27, spd)
        Click(335.32, 0.41, spd)
        Click(335.70, 0.38, spd)
        Click(336.84, 0.34, spd)
        Click(337.22, 0.34, spd)
        Click(339.49, 0.22, spd)
        Click(339.87, 0.27, spd)
        Click(340.25, 0.34, spd)
        Click(340.63, 0.27, spd)
        Click(341.01, 0.30, spd)
        Click(342.15, 0.30, spd)
        Click(342.53, 0.27, spd)
        Click(342.91, 0.22, spd)
        Click(343.29, 0.22, spd)
        Click(343.67, 0.27, spd)
        Click(344.05, 0.27, spd)
        Click(345.57, 0.22, spd)
        Click(345.95, 0.27, spd)
        Click(346.33, 0.30, spd)
        Click(346.71, 0.34, spd)
        Click(347.09, 0.38, spd)
        Click(347.47, 0.34, spd)
        Click(347.85, 0.30, spd)
        Click(348.23, 0.22, spd)
        Click(348.61, 0.19, spd)
        Click(348.99, 0.27, spd)
        Click(349.75, 0.22, spd)
        Click(351.65, 0.22, spd)
        Click(352.03, 0.27, spd)
        Click(352.41, 0.34, spd)
        Click(352.78, 0.27, spd)
        Click(353.16, 0.30, spd)
        Click(354.30, 0.34, spd)
        Click(354.68, 0.34, spd)
        Click(355.06, 0.34, spd)
        Click(355.44, 0.27, spd)
        Click(355.82, 0.22, spd)
        Click(356.20, 0.27, spd)
        Click(356.58, 0.34, spd)
        Click(356.96, 0.30, spd)
        Click(358.10, 0.22, spd)
        Click(358.48, 0.19, spd)
        Click(358.86, 0.22, spd)
        Click(359.24, 0.27, spd)
        Click(359.62, 0.41, spd)
        Click(360.00, 0.38, spd)
        Click(361.14, 0.34, spd)
        Click(361.52, 0.34, spd)
        Click(363.80, 0.22, spd)
        Click(364.18, 0.27, spd)
        Click(364.56, 0.34, spd)
        Click(364.94, 0.27, spd)
        Click(365.32, 0.30, spd)
        Click(366.46, 0.30, spd)
        Click(366.84, 0.27, spd)
        Click(367.22, 0.22, spd)
        Click(367.60, 0.22, spd)
        Click(367.97, 0.27, spd)
        Click(368.35, 0.27, spd)
        Click(369.87, 0.22, spd)
        Click(370.25, 0.27, spd)
        Click(370.63, 0.30, spd)
        Click(371.01, 0.34, spd)
        Click(371.39, 0.38, spd)
        Click(371.77, 0.34, spd)
        Click(372.15, 0.30, spd)
        Click(372.53, 0.22, spd)
        Click(372.91, 0.19, spd)
        Click(373.29, 0.27, spd)
        Click(374.05, 0.22, spd)
        Click(375.95, 0.22, spd)
        Click(376.33, 0.27, spd)
        Click(376.71, 0.34, spd)
        Click(377.09, 0.27, spd)
        Click(377.47, 0.30, spd)
        Click(378.61, 0.34, spd)
        Click(378.99, 0.34, spd)
        Click(379.37, 0.34, spd)
        Click(379.75, 0.27, spd)
        Click(380.13, 0.22, spd)
        Click(380.51, 0.27, spd)
        Click(380.89, 0.34, spd)
        Click(381.27, 0.30, spd)
        Click(382.41, 0.22, spd)
        Click(382.78, 0.19, spd)
        Click(383.16, 0.22, spd)
        Click(383.54, 0.27, spd)
        Click(383.92, 0.41, spd)
        Click(384.30, 0.38, spd)
        Click(385.44, 0.34, spd)
        Click(385.82, 0.34, spd)
        Click(388.10, 0.22, spd)
        Click(388.48, 0.27, spd)
        Click(388.86, 0.34, spd)
        Click(389.24, 0.27, spd)
        Click(389.62, 0.30, spd)
        Click(390.76, 0.34, spd)
        Click(391.14, 0.34, spd)
        Click(391.52, 0.34, spd)
        Click(391.90, 0.27, spd)
        Click(392.28, 0.22, spd)
        Click(392.66, 0.27, spd)
        Click(393.04, 0.34, spd)
        Click(393.42, 0.30, spd)
        Click(394.56, 0.22, spd)
        Click(394.94, 0.19, spd)
        Click(395.32, 0.22, spd)
        Click(395.70, 0.27, spd)
        Click(396.08, 0.41, spd)
        Click(396.46, 0.38, spd)
        Click(397.60, 0.34, spd)
        Click(397.97, 0.34, spd)
        Click(400.25, 0.22, spd)
        Click(400.63, 0.27, spd)
        Click(401.01, 0.34, spd)
        Click(401.39, 0.27, spd)
        Click(401.77, 0.30, spd)
        Click(402.91, 0.34, spd)
        Click(403.29, 0.34, spd)
        Click(403.67, 0.34, spd)
        Click(404.05, 0.27, spd)
        Click(404.43, 0.22, spd)
        Click(404.81, 0.27, spd)
        Click(405.19, 0.34, spd)
        Click(405.57, 0.30, spd)
        Click(406.71, 0.22, spd)
        Click(407.09, 0.19, spd)
        Click(407.47, 0.22, spd)
        Click(407.85, 0.27, spd)
        Click(408.23, 0.41, spd)
        Click(408.61, 0.38, spd)
        Click(415.44, 0.34, spd)
        Click(416.20, 0.34, spd)
        Offset(64)
preview()