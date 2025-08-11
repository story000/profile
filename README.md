# Portfolio Website

A dynamic portfolio website deployable on Vercel with JSON configuration.

## Features

- **Static Deployment**: No backend required, perfect for Vercel
- **Dynamic Content Loading**: All portfolio content is loaded from JSON configuration
- **Responsive Design**: Modern, dark-themed portfolio layout
- **Easy Customization**: Update content by editing the JSON file
- **External Links**: Proper external links for GitHub, LinkedIn, Notion
- **Project Filtering**: Filter projects by category (AI/Agent, Data Platform, ToB)
- **Fast Loading**: Client-side rendering with caching

## Files Structure

```
├── index.html              # Main portfolio webpage
├── portfolio_config.json   # Configuration file with all data
├── vercel.json             # Vercel deployment configuration
├── package.json            # Project metadata
└── README.md              # This file
```

## Quick Start

### Local Development

1. **Serve locally:**
   ```bash
   python -m http.server 8000
   # or
   npx serve .
   ```

2. **Open in Browser:**
   - Portfolio: http://localhost:8000

### Deploy to Vercel

1. **Install Vercel CLI:**
   ```bash
   npm i -g vercel
   ```

2. **Deploy:**
   ```bash
   vercel --prod
   ```

3. **Or deploy via GitHub:**
   - Push to GitHub repository
   - Connect repository in Vercel dashboard
   - Auto-deploy on every push

## Customization

### Update Portfolio Content

Edit `portfolio_config.json` to customize:

- **Profile Information**: Name, title, description, skills
- **Contact Details**: Email and social media links
- **Projects**: Add/edit/remove projects with their details
- **External Links**: GitHub, LinkedIn, Notion URLs

### Example Project Entry

```json
{
  "projects": [
    {
      "id": "my-project",
      "title": "My Amazing Project",
      "tagline": "Short description",
      "categories": ["ai", "b2b"],
      "tags": ["Python", "FastAPI", "React"],
      "description": {
        "background": "Problem statement",
        "competitor_analysis": "Market analysis",
        "solution": "Your solution",
        "implementation": "How you built it"
      },
      "kpis": [
        "Metric 1: +50%",
        "Metric 2: -30%"
      ],
      "role": "Your role description",
      "links": {
        "demo": "https://your-demo.com",
        "screenshots": "https://your-screenshots.com"
      }
    }
  ]
}
```

## Features Implemented

✅ **JSON Configuration**: All content externalized to JSON file  
✅ **Static Deployment**: No backend needed, perfect for Vercel  
✅ **Dynamic Frontend**: JavaScript loads data from JSON file  
✅ **External Links**: Proper links to GitHub, LinkedIn, Notion  
✅ **Button Refinements**: Contact email, demo links, screenshot links  
✅ **Project Filtering**: Filter by AI/Agent, Data Platform, ToB categories  
✅ **Responsive Design**: Works on desktop and mobile  
✅ **Error Handling**: Graceful loading states and error messages  
✅ **Vercel Ready**: Optimized for Vercel deployment  

## Development

- Serve locally with any static server
- Edit `portfolio_config.json` and refresh the page to see changes
- No build process needed - pure HTML/CSS/JavaScript
- JSON file is cached for better performance

## Vercel Deployment Benefits

- **Zero Configuration**: Just deploy the files
- **Global CDN**: Fast loading worldwide
- **Automatic HTTPS**: SSL certificates managed automatically
- **Custom Domains**: Easy to set up custom domains
- **GitHub Integration**: Auto-deploy on push