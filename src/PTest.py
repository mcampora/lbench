import sys

def bubblesort(tab):
	#c = 0
	n = len(tab)
	for i in range(n - 1):
		for j in range(i + 1, n):
			if tab[i] > tab[j]:
				#aux = tab[i]
				#tab[i] = tab[j]
				#tab[j] = aux
				tab[i],tab[j] = tab[j],tab[i]
				#c = c + 1
	#print(c)
			
if __name__ == "__main__":
	rep = 1
	if len(sys.argv) > 1:
		rep = int(sys.argv[1])
	
	for r in range(rep):
		tab = [797, 881, 315, 468, 479, 101, 213, 214, 391, 601, 684, 70, 123, 200, 964, 967, 710, 974, 258, 344, 9, 640, 971, 813, 361, 807, 411, 652, 353, 41, 431, 49, 933, 514, 155, 718, 341, 560, 550, 158, 291, 61, 413, 262, 772, 502, 363, 660, 137, 736, 831, 221, 311, 254, 941, 481, 839, 241, 104, 150, 449, 862, 128, 501, 987, 620, 646, 301, 64, 594, 746, 1, 943, 327, 701, 729, 765, 240, 748, 67, 662, 228, 532, 81, 857, 836, 167, 452, 169, 2, 465, 825, 430, 187, 364, 818, 202, 875, 779, 671, 220, 432, 792, 414, 902, 782, 32, 624, 293, 649, 863, 751, 178, 672, 554, 664, 627, 500, 616, 446, 972, 731, 785, 614, 487, 656, 134, 632, 38, 566, 207, 536, 374, 581, 63, 331, 527, 764, 790, 173, 406, 890, 950, 968, 112, 966, 691, 27, 995, 889, 352, 227, 588, 404, 189, 335, 346, 923, 259, 673, 348, 33, 767, 869, 993, 88, 332, 98, 448, 998, 285, 856, 675, 75, 196, 389, 255, 477, 508, 182, 120, 846, 23, 556, 708, 981, 592, 634, 678, 426, 618, 817, 697, 109, 132, 689, 469, 583, 852, 611, 25, 265, 571, 962, 891, 654, 305, 538, 619, 841, 8, 24, 916, 907, 480, 655, 837, 679, 589, 222, 622, 376, 570, 471, 930, 324, 225, 819, 87, 359, 445, 585, 828, 297, 904, 125, 969, 829, 717, 232, 851, 861, 29, 638, 485, 110, 692, 483, 204, 845, 40, 153, 530, 48, 370, 906, 747, 433, 996, 495, 459, 932, 415, 156, 303, 428, 343, 642, 533, 665, 521, 347, 999, 457, 496, 56, 467, 333, 721, 310, 994, 921, 438, 666, 506, 808, 253, 143, 231, 609, 574, 936, 115, 704, 264, 911, 349, 674, 983, 17, 978, 801, 410, 903, 217, 216, 455, 162, 82, 194, 523, 898, 206, 949, 894, 453, 812, 561, 774, 279, 551, 723, 369, 872, 44, 564, 683, 607, 257, 965, 74, 403, 794, 117, 847, 707, 937, 268, 750, 407, 874, 494, 193, 260, 752, 572, 963, 961, 569, 738, 702, 271, 13, 896, 498, 833, 144, 598, 647, 804, 873, 12, 489, 557, 281, 244, 85, 62, 473, 418, 236, 555, 617, 759, 578, 503, 756, 360, 460, 946, 450, 421, 516, 106, 518, 50, 653, 451, 773, 191, 18, 111, 394, 680, 288, 71, 435, 229, 577, 329, 522, 294, 913, 447, 758, 79, 985, 549, 547, 409, 372, 947, 663, 515, 880, 929, 208, 927, 942, 388, 318, 362, 563, 753, 7, 492, 103, 141, 970, 842, 960, 314, 510, 600, 677, 659, 90, 977, 151, 871, 641, 272, 682, 924, 417, 99, 205, 0, 957, 768, 910, 755, 86, 371, 16, 392, 513, 442, 425, 787, 934, 635, 223, 190, 437, 234, 199, 639, 535, 172, 705, 412, 497, 100, 788, 805, 726, 623, 77, 761, 613, 803, 355, 835, 796, 245, 317, 373, 482, 735, 436, 548, 154, 559, 298, 345, 339, 52, 657, 325, 512, 838, 695, 780, 94, 900, 714, 198, 34, 860, 696, 740, 357, 230, 770, 713, 830, 859, 397, 528, 667, 821, 844, 955, 304, 575, 185, 416, 980, 827, 302, 247, 127, 21, 919, 762, 322, 771, 22, 540, 579, 988, 742, 766, 958, 615, 826, 278, 183, 823, 832, 769, 152, 811, 730, 6, 918, 140, 276, 925, 399, 419, 626, 267, 186, 145, 312, 43, 10, 694, 931, 584, 161, 239, 149, 116, 816, 248, 470, 733, 475, 165, 939, 926, 365, 147, 990, 876, 249, 59, 545, 565, 57, 337, 700, 400, 384, 630, 408, 850, 401, 215, 728, 591, 989, 289, 309, 905, 402, 95, 261, 621, 897, 703, 91, 858, 378, 130, 434, 809, 793, 210, 320, 610, 885, 883, 505, 180, 283, 287, 238, 744, 582, 280, 688, 474, 643, 810, 815, 602, 849, 73, 251, 176, 350, 719, 89, 266, 177, 385, 15, 820, 975, 55, 636, 976, 393, 270, 342, 20, 959, 65, 102, 864, 922, 800, 338, 499, 60, 78, 953, 543, 439, 544, 948, 139, 224, 973, 218, 743, 567, 58, 423, 940, 763, 754, 992, 587, 326, 706, 160, 273, 956, 676, 982, 507, 424, 458, 390, 242, 336, 887, 422, 952, 991, 590, 912, 379, 174, 745, 11, 951, 30, 382, 741, 899, 776, 866, 798, 334, 328, 308, 157, 603, 93, 997, 263, 179, 243, 461, 290, 686, 170, 105, 440, 114, 984, 108, 781, 358, 219, 286, 537, 865, 319, 54, 777, 712, 277, 233, 444, 612, 944, 867, 908, 356, 66, 915, 126, 235, 80, 252, 593, 658, 122, 188, 443, 685, 386, 553, 901, 909, 606, 197, 250, 878, 135, 456, 637, 226, 799, 420, 511, 734, 526, 720, 539, 159, 650, 330, 121, 732, 786, 562, 757, 464, 892, 834, 491, 775, 367, 917, 517, 113, 306, 814, 136, 737, 604, 19, 669, 26, 118, 525, 284, 648, 472, 690, 822, 37, 725, 668, 709, 484, 806, 299, 295, 595, 629, 466, 383, 986, 274, 119, 96, 53, 855, 840, 914, 171, 31, 405, 722, 462, 47, 596, 256, 476, 269, 463, 478, 824, 760, 323, 784, 307, 296, 687, 868, 72, 546, 321, 68, 853, 886, 573, 282, 429, 520, 163, 486, 608, 882, 558, 76, 368, 398, 351, 97, 879, 645, 531, 493, 802, 552, 542, 387, 568, 39, 36, 586, 92, 791, 69, 935, 3, 5, 628, 203, 661, 681, 576, 711, 146, 396, 504, 316, 739, 84, 488, 644, 749, 209, 884, 395, 888, 14, 633, 534, 580, 4, 340, 83, 129, 716, 698, 509, 354, 142, 138, 131, 124, 184, 46, 246, 893, 292, 237, 795, 789, 380, 42, 870, 45, 670, 168, 724, 783, 28, 51, 375, 211, 529, 133, 181, 699, 381, 895, 928, 599, 778, 366, 212, 441, 920, 275, 175, 148, 524, 490, 605, 313, 107, 201, 877, 631, 938, 979, 454, 715, 693, 854, 166, 195, 651, 727, 192, 164, 597, 300, 848, 843, 377, 519, 541, 954, 625, 945, 35, 427]
		bubblesort(tab)
	
	#print(tab)
	#print(r)


