# Security Guidelines

## 🔒 Sensitive Information

This repository is **public**. Never commit or document the following:

### ❌ Do Not Expose Publicly

1. **Analytics Tracking IDs**
   - Google Analytics ID
   - Facebook Pixel ID
   - Other tracking codes
   - *Note: While these are visible in live site HTML, don't document them in README/docs*

2. **API Keys & Secrets**
   - Netlify deploy keys
   - ImageKit API keys
   - Any authentication tokens

3. **Internal Email Addresses**
   - Team member emails
   - Internal distribution lists
   - *Exception: Public contact emails (partners@) are OK*

4. **Deployment Credentials**
   - Netlify site IDs
   - Build hook URLs
   - Environment variables

5. **Business Intelligence**
   - Traffic numbers
   - Conversion rates
   - User metrics
   - Revenue data

## ✅ Safe to Share

- Tech stack (frameworks, libraries)
- Build commands (`npm run build`)
- Project structure
- Branding guidelines
- Public domain (tixhawk.com)
- Hosting platform name (Netlify)

## 📋 Best Practices

1. **Analytics IDs**: Store in HTML files only (necessary for functionality)
2. **Secrets**: Use Netlify environment variables
3. **Documentation**: Keep sensitive info in private team docs
4. **Code Review**: Check for accidentally committed secrets before push

## 🚨 If Secrets Are Exposed

If you accidentally commit sensitive information:

1. **Immediately rotate** the exposed credentials
2. **Remove from git history** using `git filter-branch` or BFG Repo-Cleaner
3. **Update** all systems using the old credentials
4. **Document** the incident in internal security log

## 📝 For Team Members

Internal documentation with sensitive info should be stored in:
- Private team wiki
- Password manager (shared vault)
- Internal Notion/Confluence workspace

**Never** in this public repository.

---

**Questions?** Contact security@digerstudios.com
