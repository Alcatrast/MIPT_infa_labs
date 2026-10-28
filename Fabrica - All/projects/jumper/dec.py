import re
import matplotlib.pyplot as plt
import numpy as np

# ---------- чтение файла ----------
with open(r"C:\Users\LaL\Desktop\jumper\hh.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# ---------- хранилища ----------
A_raw = []
A_cal = []
A_filt = []
V = []
R = []

# ---------- regex ----------
vec_re = re.compile(r"([-+]?\d*\.\d+|\d+)")

def parse_vec(line):
    nums = vec_re.findall(line)
    return [float(n) for n in nums]

# ---------- парсинг ----------
for line in lines:
    if line.startswith("A raw"):
        A_raw.append(parse_vec(line))
    elif line.startswith("A cal"):
        A_cal.append(parse_vec(line))
    elif line.startswith("A filt"):
        A_filt.append(parse_vec(line))
    elif line.startswith("V:"):
        V.append(parse_vec(line))
    elif line.startswith("R:"):
        R.append(parse_vec(line))

A_raw = np.array(A_raw)
A_cal = np.array(A_cal)
A_filt = np.array(A_filt)
V = np.array(V)
R = np.array(R)

t = np.arange(len(A_raw))  # индекс времени

print("Samples:", len(t))

# =========================================================
# ОКНО 1 — КИНЕМАТИКА
# =========================================================
fig1, axs1 = plt.subplots(3, 3, figsize=(16, 10))
fig1.suptitle("Trajectory / Velocity / Acceleration")

labels = ["X", "Y", "Z"]

for i in range(3):
    axs1[i, 0].plot(t, R[:, i])
    axs1[i, 0].set_title(f"Position {labels[i]}")
    axs1[i, 0].grid()

    axs1[i, 1].plot(t, V[:, i])
    axs1[i, 1].set_title(f"Velocity {labels[i]}")
    axs1[i, 1].grid()

    axs1[i, 2].plot(t, A_filt[:, i])
    axs1[i, 2].set_title(f"Acceleration {labels[i]}")
    axs1[i, 2].grid()

plt.tight_layout()

# =========================================================
# ОКНО 2 — СЕНСОРНЫЕ ДАННЫЕ
# =========================================================
fig2, axs2 = plt.subplots(3, 3, figsize=(16, 10))
fig2.suptitle("Accel raw / calibrated / filtered")

for i in range(3):
    axs2[i, 0].plot(t, A_raw[:, i])
    axs2[i, 0].set_title(f"A raw {labels[i]}")
    axs2[i, 0].grid()

    axs2[i, 1].plot(t, A_cal[:, i])
    axs2[i, 1].set_title(f"A cal {labels[i]}")
    axs2[i, 1].grid()

    axs2[i, 2].plot(t, A_filt[:, i])
    axs2[i, 2].set_title(f"A filt {labels[i]}")
    axs2[i, 2].grid()

plt.tight_layout()
plt.show()