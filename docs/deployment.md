# 站点结构与构建

```text
literature-map*.html     中英文论文关系图
knowledge-network*.html  中英文知识网络
assets/                 共享导航与样式
literature/             文献概括与逐篇阅读记录
knowledge/              知识说明与推导
papers/                 PDF 文献库
scripts/                公开内容检查与站点打包
docs/                   维护说明
.github/workflows/      GitHub Pages 工作流
```

网页包含已整理的数据、交互代码与离线公式。公开仓库的构建不需要本地研究材料，也不会重新生成研究内容。新增顶层导航只需修改 `assets/site-nav.js` 的页面列表。

本地阅读：运行 `python -m http.server 8000`，打开 `http://localhost:8000/literature-map.html`，可以访问本地 PDF。

检查公开内容：运行 `python scripts/audit_public.py`。检查内容包含发布目录边界、私有链接、网页数据与知识引用的一致性。

发布预览：运行 `python scripts/build_site.py`，再运行 `python -m http.server 8000 --directory dist`。`dist/` 是可重新生成的发布目录，不提交版本库。首页进入论文关系图，保留哈希定位；资源路径支持 GitHub Pages 仓库子路径。

网页部署产物不包含 PDF。PDF 按钮指向论文原始来源，Markdown 参考链接指向当前提交的 GitHub 渲染页。打包其他仓库可指定 `--repository owner/repo --ref main`。

GitHub 设置：打开仓库 **Settings → Pages**，在 **Build and deployment → Source** 中选择 **GitHub Actions**。本仓库已有 `.github/workflows/pages.yml`，无需额外选择模板或创建工作流。

将公开内容推送到 `main` 后，工作流会自动构建并部署 `dist/`；也可在 **Actions → Deploy Pages → Run workflow** 中手动运行。部署成功后在 **Settings → Pages** 查看站点地址。`dist/` 无需手动上传，工作流会生成它。
