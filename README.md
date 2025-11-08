# TicketHawk Landing Page

Last-minute concert and event ticket alert service. Never miss sold-out concerts again.

## 🎯 Branding Notice

**IMPORTANT**: The brand name is **TicketHawk** (not TixHawk).

- **TicketHawk** = Official brand name (use in all customer-facing content)
- **TixHawk** = Domain shorthand at tixhawk.com (use in SEO/metadata only)

📖 **See [BRANDING.md](./BRANDING.md) for complete guidelines**

## 🚀 Quick Start

```bash
# Install dependencies
npm install

# Build CSS (Tailwind)
npm run build

# Development (watch mode)
npm run dev
```

## 📁 Project Structure

```
tixhawk/
├── index.html              # Main landing page
├── thanks.html             # Waitlist confirmation page
├── styles.css              # Generated Tailwind CSS (do not edit directly)
├── src/
│   └── input.css          # Tailwind source (edit this)
├── media_assets/
│   ├── fav.png            # Favicon
│   ├── Video_*.mp4        # Hero videos (mobile + desktop)
├── og-image.png           # Social media preview image (1200x630)
├── tailwind.config.js     # Tailwind configuration
├── netlify.toml           # Netlify deployment config
├── BRANDING.md            # Brand guidelines ⚠️ READ THIS
└── README.md              # This file
```

## 🎨 Design System

- **Primary Gradient**: Purple (#667eea) to Pink (#764ba2)
- **Typography**: System fonts (ui-sans-serif)
- **Framework**: Tailwind CSS 3.4.10
- **Responsive**: Mobile-first design

## 📝 Key Features

- ✅ Early access waitlist with Netlify Forms
- ✅ Mobile-optimized (separate vertical/horizontal videos)
- ✅ SEO optimized with structured data (Schema.org)
- ✅ Social media ready (OG image, Twitter cards)
- ✅ Analytics integrated (Google Analytics, Facebook Pixel)
- ✅ Anti-scalper messaging for real fans

## 🔧 Development

### Building Styles

The `styles.css` file is generated from `src/input.css` using Tailwind:

```bash
npm run build     # Production build (minified)
npm run dev       # Watch mode for development
```

**Note**: Never edit `styles.css` directly - always edit `src/input.css`

### Deployment

Deployed on Netlify. Push to main branch triggers automatic deployment.

Build command: `npm run build`
Publish directory: `.` (root)

## 📊 Analytics & Configuration

Analytics tracking IDs and sensitive configuration are stored in the HTML files and deployment environment.

**For internal team reference:**
- See `index.html` for analytics integration
- Contact admin for access to analytics dashboards

## 🔒 Tech Stack

- **Domain**: https://tixhawk.com
- **Hosting**: Netlify
- **Form Handler**: Netlify Forms
- **CDN**: ImageKit (videos)
- **CSS Framework**: Tailwind CSS 3.4.10
- **Analytics**: Google Analytics, Facebook Pixel

## ⚠️ Important Notes

1. **Security**: This is a public repo - see [SECURITY.md](./SECURITY.md) for what not to commit
2. **Branding**: Always use "TicketHawk" in user-facing content (see BRANDING.md)
3. **CSS**: Don't edit styles.css directly - use src/input.css
4. **Videos**: Stored on ImageKit CDN, not in repo (see media_assets/ for local copies)
5. **OG Image**: Regenerate if branding/tagline changes

## 📞 Contact

For partnership inquiries, visit https://tixhawk.com

Built by [Diger Studios LLC](https://digerstudios.com)

---

**Last Updated**: 2025-11-08
