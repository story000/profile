# 项目截图管理说明

## 📁 文件夹结构

```
images/
├── aivc-system/          # AIVC 多智能体研究系统
├── quant-ml-system/      # 量化交易ML预测系统  
├── blockchain-graph-mining/  # 区块链图挖掘系统
└── graph-algorithm-optimization/  # 图算法优化研究
```

## 🖼️ 使用方法

1. **添加图片**：将项目截图放入对应的项目文件夹中
2. **命名建议**：使用有意义的中文或英文名称（如：`系统概览.png`、`用户界面.png`等）
3. **支持格式**：PNG, JPG, JPEG, GIF, WebP, BMP, SVG
4. **生成列表**：添加图片后运行 `python3 generate-image-list.py`
5. **部署更新**：将生成的 `images-list.json` 一起部署

## ⚙️ 自动化流程

```bash
# 1. 添加图片到项目文件夹
cp 我的截图.png images/aivc-system/系统界面.png

# 2. 重新生成图片列表
python3 generate-image-list.py

# 3. 部署到 Vercel（会自动包含 images-list.json）
vercel --prod
```

## 📝 当前状态

- **aivc-system**: 4张图片 ✅
  - 可交互界面.png
  - 数据标注中心.png  
  - 系统评测界面.png
  - 自动化页面.png
- **其他项目**: 暂无图片

## 🚀 Vercel 部署优势

- ✅ 纯静态文件，无需服务器
- ✅ 全球CDN加速
- ✅ 自动HTTPS
- ✅ 图片文件名直接作为标题显示