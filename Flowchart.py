import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.sankey import Sankey

fig, ax = plt.subplots(figsize=(8, 6))

# Create boxes for the flowchart with annotations
ax.annotate('Satellite Data Acquisition', xy=(0.5, 0.9), xytext=(0.5, 0.9),
            bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightblue"), ha='center', fontsize=12)

ax.annotate('Ground-based Data Collection', xy=(0.1, 0.7), xytext=(0.1, 0.7),
            bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgreen"), ha='center', fontsize=12)

ax.annotate('Traffic, Weather, \n and Contextual Data', xy=(0.9, 0.7), xytext=(0.9, 0.7),
            bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightyellow"), ha='center', fontsize=12)

ax.annotate('Data Preprocessing \n & Integration', xy=(0.5, 0.55), xytext=(0.5, 0.55),
            bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightcoral"), ha='center', fontsize=12)

ax.annotate('AI/ML Model Training \n (CNN/GAN)', xy=(0.5, 0.4), xytext=(0.5, 0.4),
            bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightpink"), ha='center', fontsize=12)

ax.annotate('Prediction: High-Resolution \n Air Quality Map', xy=(0.5, 0.25), xytext=(0.5, 0.25),
            bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"), ha='center', fontsize=12)

ax.annotate('Real-time Deployment \n & Visualization', xy=(0.5, 0.1), xytext=(0.5, 0.1),
            bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightblue"), ha='center', fontsize=12)

# Draw arrows between the steps
ax.arrow(0.5, 0.85, 0, -0.1, head_width=0.02, head_length=0.03, fc='black', ec='black')
ax.arrow(0.1, 0.65, 0.3, -0.05, head_width=0.02, head_length=0.03, fc='black', ec='black')
ax.arrow(0.9, 0.65, -0.3, -0.05, head_width=0.02, head_length=0.03, fc='black', ec='black')
ax.arrow(0.5, 0.5, 0, -0.1, head_width=0.02, head_length=0.03, fc='black', ec='black')
ax.arrow(0.5, 0.35, 0, -0.1, head_width=0.02, head_length=0.03, fc='black', ec='black')
ax.arrow(0.5, 0.2, 0, -0.1, head_width=0.02, head_length=0.03, fc='black', ec='black')

ax.set_title('Technical Flowchart for Downscaling Air Quality Maps using AI/ML', fontsize=14)
ax.axis('off')
plt.show()
