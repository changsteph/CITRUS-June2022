import matplotlib.pyplot as plt

wind_mean_703 = [3.8439, 4.0899, 4.3602, 4.8278, 4.5749, 5.1531, 5.3453, 5.2483, 4.5631, 4.2667, 4.2173, 4.1329]
wind_mean_840 = [3.423, 3.7533, 3.934, 4.0726, 3.7081, 4.071, 4.231, 4.0671, 3.647, 3.4908, 3.6486, 3.5187]
wind_mean_842 = [3.1212, 3.3063, 3.5251, 3.4585, 3.1568, 3.2718, 3.3542, 3.2869, 3.1155, 3.1137, 3.1975, 3.1639]
wind_mean_911 = [4.8031, 5.0326, 5.2612, 6.2176, 6.0012, 6.6993, 6.5318, 6.3407, 5.8794, 5.3824, 5.7731, 5.1664]

temp_mean_703 = [23.071603633667042, 23.203731930321894, 23.665739710789765, 24.75887237415775, 25.58917050691244,
                 26.777777777777782, 27.44141705069124, 27.81094470046083, 27.53845238095238, 26.84793010752688,
                 25.46172619047619, 24.051958525345622]
temp_mean_840 = [22.9523334530335, 22.89845849766315, 23.200545104908805, 24.040703712071934, 24.74102554796334,
                 25.643042514637333, 26.097872513116197, 26.59960561584234, 26.727184488563797, 26.183349053748298,
                 24.898165001027074, 23.75592570144694]
temp_mean_841 = [22.25235413460803, 21.972517384802988, 22.506109680159334, 22.972154317186646, 23.80750870754812,
                 25.24433477348862, 25.440510486825, 25.762196823508585, 25.821351314310395, 25.392489154678245,
                 23.938920685668563, 23.119360799574782]
temp_mean_901 = [22.08718574546558, 22.032484204543497, 22.358555792838317, 23.13284042700872, 23.787254934581547,
                 24.863170005282072, 25.38120821812596, 25.76415072530752, 25.916493352349793, 25.348307758176908,
                 24.16226573786887, 23.0219198510064]

months_names = ["January", "February", "March", "April", "May", "June", "July", "August",
                "September", "October", "November", "December"]

wind_station_names = [
    "703 HONOLULU INTERNATIONAL AIRPORT Wind Speeds",
    "840 KANEOHE BAY MCAS Wind Speeds",
    "842.8 MAKUA RANGE Wind Speeds",
    "911.1 KII Wind Speeds"
]

temp_station_names = [
    "703 HONOLULU INTERNATIONAL AIRPORT Temperatures",
    "840 KANEOHE BAY MCAS Temperatures",
    "841.16 CAMP ERDMAN Temperatures",
    "901.2 KII KAHUKU Temperatures"
]
plt.plot(temp_mean_703, color="magenta", marker="o", linestyle="dashed", markersize=10)
for i, value in enumerate(temp_mean_703):
    plt.annotate(str(round(value, 3)), (i, value + 0.05))
plt.plot(temp_mean_840, color="green", marker="o", linestyle="dashed", markersize=10)
for i, value in enumerate(temp_mean_840):
    plt.annotate(str(round(value, 3)), (i, value + 0.05))
plt.plot(temp_mean_841, color="blue", marker="o", linestyle="dashed", markersize=10)
for i, value in enumerate(temp_mean_841):
    plt.annotate(str(round(value, 3)), (i, value + 0.05))
plt.plot(temp_mean_901, color="purple", marker="o", linestyle="dashed", markersize=10)
for i, value in enumerate(temp_mean_901):
    plt.annotate(str(round(value, 3)), (i, value + 0.05))
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], months_names)
plt.ylim(bottom=21, top=29)
plt.xlabel("Months", fontsize=15)
plt.ylabel("Temperature (C)", fontsize=15)
plt.title("Mean Oahu Temperatures", fontsize=25)
plt.legend(["703 HNL", "840 Kaneohe Bay", "841.16 Camp Erdman", "901.1 Kii"], title="Stations", loc='upper left')
plt.grid(True)
# plt.savefig("MeanWindSpeeds.png")
plt.show()

# plt.plot(wind_mean_703, color="magenta", marker="o", linestyle="dashed", markersize=10)
# for i, value in enumerate(wind_mean_703):
#     plt.annotate(str(round(value, 3)), (i, value + 0.05))
# plt.plot(wind_mean_840, color="green", marker="o", linestyle="dashed", markersize=10)
# for i, value in enumerate(wind_mean_840):
#     plt.annotate(str(round(value, 3)), (i, value + 0.05))
# plt.plot(wind_mean_842, color="blue", marker="o", linestyle="dashed", markersize=10)
# for i, value in enumerate(wind_mean_842):
#     plt.annotate(str(round(value, 3)), (i, value + 0.05))
# plt.plot(wind_mean_911, color="purple", marker="o", linestyle="dashed", markersize=10)
# for i, value in enumerate(wind_mean_911):
#     plt.annotate(str(round(value, 3)), (i, value + 0.05))
# plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], months_names)
# plt.ylim(bottom=1.5, top=7.5)
# plt.xlabel("Months", fontsize=15)
# plt.ylabel("Wind Speed (m/s)", fontsize=15)
# plt.title("Mean Oahu Wind Speeds", fontsize=25)
# plt.legend(["703 HNL", "840 Kaneohe Bay", "842.8 Makua Range", "911.1 Kii"], title="Stations", loc='lower left')
# plt.grid(True)
# # plt.savefig("MeanWindSpeeds.png")
# plt.show()




















