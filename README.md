# PC_VO
PC-VO: Uncertainty-Aware Deep Visual Odometry with Exhaustive Pose Consistency

![overview](./assets/overview.png)

## ⚙️Code under construction...

## 📊Evaluation

### Env Setup

```bash
conda create -n pcvo python=3.9 & conda activate pcvo
pip install evo matplotlib
```

### Visualize KITTI Results

* For KITTI validation split(03/05/06/07/10):

```bash
cd results/kitti/0x/
evo_traj kitti --ref GT.txt ORB-SLAM.txt DeepVO.txt Ours.txt MDN-VO.txt -vsap --plot_mode xz --align_origin #(optional)
```
![kitti_comparison_eval](./assets/kitti/kitti_comparison_eval.png)

* For KITTI others:

![kitti_comparison_other](./assets/kitti/kitti_comparison_other.png)

##### Visualize nuScenes Results
* for nuScenes(0572/0972/0999)

```bash
cd results/nuscenes/0XXX/
evo_traj kitti --ref GT.txt ORB-SLAM.txt DeepVO.txt Ours.txt MDN-VO.txt -vsap --plot_mode xz --align_origin #(optional)
```

![nuscenes_comparison](./assets/nuscenes/nuscenes_comparison.png)

##### Visualize Uncertainty

```bash
python draw_uncert_ablation.py
```

![uncert_ablation](./assets/uncert/uncert_ablation.png)
