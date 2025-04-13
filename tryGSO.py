import sys
from pathlib import Path

project_root = Path(__file__).parent.parent  # 假设 tryGSO.py 在 examples/ 目录下
sys.path.append(str(project_root))

import requests
import os
import kubric as kb
from kubric import core
from kubric.core import assets
from kubric.simulator import PyBullet
from kubric.renderer import Blender

print("当前工作目录:", os.getcwd()) 
# 初始化 Kubric 场景
scene = kb.Scene(resolution=(512, 512))
simulator = PyBullet(scene)
renderer = Blender(scene)

# 加载模型到场景
car = kb.core.FileBasedObject(
    asset_id="hatchback_red",
    simulation_filename="/kubric/kubric/models/hatchback_red.glb",  # 物理仿真模型路径
    render_filename="/kubric/kubric/models/hatchback_red.glb",       # 渲染模型路径）
)
scene.add(car)

# 添加光源与摄像机
scene.add(kb.DirectionalLight(position=(3, 4, 5), look_at=(0, 0, 0), intensity=1.5))
scene.camera = kb.PerspectiveCamera(position=(5, 5, 5), look_at=(0, 0, 1))

# 运行物理仿真
simulator.run(frame_end=60)

# 渲染输出
renderer.save_state("output/hatchback_sim.png")

