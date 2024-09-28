import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.sankey import Sankey

# Initialize figure
fig, ax = plt.subplots(figsize=(10, 12))
ax.set_title('Satellite-Based Air Quality Downscaling using AI/ML Models', fontsize=14)

# Define the boxes and their positions
boxes = {
    "Start": (0.5, 0.95),
    "Satellite Data (NASA, ESA)": (0.2, 0.85),
    "Ground-based Data (Sensors, Weather APIs, Land Use Data)": (0.8, 0.85),
    "Data Preprocessing and Cloud Integration": (0.5, 0.75),
    "AI/ML Model Development": (0.5, 0.65),
    "Model Training and Validation": (0.5, 0.55),
    "Prediction and Validation": (0.5, 0.45),
    "Deployment and Real-time Monitoring": (0.5, 0.35),
    "Web Development": (0.5, 0.25),
    "End": (0.5, 0.15)
}

# Create rectangles for each box
for box, pos in boxes.items():
    ax.text(pos[0], pos[1], box, ha='center', va='center', fontsize=10, 
            bbox=dict(facecolor='lightblue', edgecolor='black', boxstyle='round,pad=0.5'))

# Draw arrows between boxes
arrowprops = dict(facecolor='black', edgecolor='black', arrowstyle="->", lw=1)

# Horizontal arrows
ax.annotate('', xy=(0.3, 0.85), xytext=(0.45, 0.85), arrowprops=arrowprops)
ax.annotate('', xy=(0.7, 0.85), xytext=(0.55, 0.85), arrowprops=arrowprops)

# Vertical arrows
for start, end in [("Start", "Satellite Data (NASA, ESA)"), 
                   ("Satellite Data (NASA, ESA)", "Data Preprocessing and Cloud Integration"),
                   ("Ground-based Data (Sensors, Weather APIs, Land Use Data)", "Data Preprocessing and Cloud Integration"),
                   ("Data Preprocessing and Cloud Integration", "AI/ML Model Development"),
                   ("AI/ML Model Development", "Model Training and Validation"),
                   ("Model Training and Validation", "Prediction and Validation"),
                   ("Prediction and Validation", "Deployment and Real-time Monitoring"),
                   ("Deployment and Real-time Monitoring", "Web Development"),
                   ("Web Development", "End")]:
    start_pos = boxes[start]
    end_pos = boxes[end]
    ax.annotate('', xy=(start_pos[0], start_pos[1] - 0.05), 
                xytext=(end_pos[0], end_pos[1] + 0.05), arrowprops=arrowprops)

# Hide axes
ax.axis('off')

# Show plot
plt.show()
