# Step-by-Step Guide: Deploying advisee.ai on Vercel

This guide will walk you through deploying your advisee.ai landing page on Vercel for free and connecting it to your GoDaddy domain.

## Prerequisites
- Your GoDaddy account with access to advisee.ai domain
- A GitHub account (free)
- A Vercel account (free)

## Step 1: Prepare Your Landing Page

1. Create a new folder on your computer named `advisee-site`
2. Create a file named `index.html` inside this folder
3. Copy and paste the HTML code provided earlier into this file
4. Save the file

## Step 2: Create a GitHub Repository

1. Go to [GitHub](https://github.com/) and log in (or create an account if needed)
2. Click the "+" icon in the top-right corner and select "New repository"
3. Name your repository (e.g., "advisee-website")
4. Add a description (optional)
5. Keep the repository Public (for free hosting)
6. Click "Create repository"

## Step 3: Upload Your Code to GitHub

### Option A: Using GitHub Desktop (Easiest)
1. Download and install [GitHub Desktop](https://desktop.github.com/)
2. Log in with your GitHub account
3. Click "File" → "Clone repository" and select your new repository
4. Choose a location on your computer to save it
5. Copy your `index.html` file into this folder
6. In GitHub Desktop, you'll see the file appear in the "Changes" tab
7. Add a commit message like "Initial landing page"
8. Click "Commit to main"
9. Click "Push origin" to upload to GitHub

### Option B: Using Git Command Line
1. Install Git if you don't have it
2. Open Terminal/Command Prompt
3. Navigate to your project folder:
   ```
   cd path/to/advisee-site
   ```
4. Initialize Git and connect to your repository:
   ```
   git init
   git remote add origin https://github.com/yourusername/advisee-website.git
   ```
5. Add your files, commit, and push:
   ```
   git add .
   git commit -m "Initial landing page"
   git push -u origin main
   ```

## Step 4: Deploy on Vercel

1. Go to [Vercel](https://vercel.com/) and sign up/log in (you can sign up with your GitHub account)
2. Once logged in, click "Add New..." → "Project"
3. Vercel will show a list of your GitHub repositories - find and select "advisee-website"
4. In the configuration screen:
   - Framework Preset: Select "Other" (or leave as default)
   - Root Directory: Leave as default (/)
   - Build Command: Leave empty (for simple HTML sites)
   - Output Directory: Leave empty
5. Click "Deploy"
6. Wait a few moments for deployment to complete
7. Vercel will provide a URL (something like `advisee-website.vercel.app`) where you can preview your site

## Step 5: Connect Your Custom Domain (advisee.ai)

1. In your Vercel dashboard, click on your newly deployed project
2. Go to "Settings" → "Domains"
3. Enter your domain: `advisee.ai`
4. Click "Add"
5. Vercel will provide DNS configuration instructions - you'll need to update these in GoDaddy

## Step 6: Update DNS Settings in GoDaddy

1. Log in to your GoDaddy account
2. Navigate to "My Products" → "Domains" and select advisee.ai
3. Click "DNS" or "Manage DNS"
4. You'll need to add the following records (based on what Vercel provides):

   ### Option A: Using A Records (Recommended)
   - Find and remove any existing A records for @ (or create new ones if none exist)
   - Add A records pointing to Vercel's IP addresses:
     ```
     Type: A
     Name: @
     Value: 76.76.21.21
     TTL: 1 hour (or default)
     ```

   ### Option B: Using CNAME Records (Alternative)
   - Find and remove any existing CNAME records (except email-related ones)
   - Add a CNAME record:
     ```
     Type: CNAME
     Name: www
     Value: cname.vercel-dns.com
     TTL: 1 hour (or default)
     ```

5. Save your changes

## Step 7: Verify Domain Connection

1. Return to Vercel dashboard → Domains section
2. Vercel will show verification status for your domain
3. It may take 24-48 hours for DNS changes to fully propagate
4. Once verified, you'll see a green "Valid Configuration" status

## Step 8: Test Your Site

1. Open a web browser and go to advisee.ai
2. You should see your landing page with the two buttons
3. Test both buttons to ensure they correctly redirect to your Substack and Meetup pages

## Making Future Updates

Whenever you want to update your site:

1. Edit the `index.html` file locally
2. Commit and push changes to GitHub (using GitHub Desktop or command line)
3. Vercel will automatically detect changes and redeploy your site

## Troubleshooting

### Domain Not Connecting
- Double-check DNS settings in GoDaddy
- Verify you've removed conflicting DNS records
- Wait 24-48 hours for propagation
- In Vercel, try clicking "Refresh" in the Domains section

### Site Not Updating
- Ensure changes are pushed to the correct GitHub repository
- Check Vercel deployment logs for errors
- Try a hard refresh in your browser (Ctrl+F5 or Cmd+Shift+R)

## Additional Resources

- [Vercel Documentation](https://vercel.com/docs)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [GoDaddy DNS Management Help](https://www.godaddy.com/help/manage-dns-records-680)
