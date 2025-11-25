# PowerShell helper to initialize git, commit and show push commands for GitHub + Render deployment
# Run this from the project root: cd c:\Users\abdo\python261

Write-Host "1) Initialize git and commit changes"
git init
git add .
git commit -m "Initial commit: Flask e-commerce"

Write-Host "\n2) Create remote and push (replace placeholders if needed)"
Write-Host "If you have GitHub CLI (gh) installed, you can run:"
Write-Host "  gh repo create <USERNAME>/<REPO> --public --source=. --remote=origin --push"
Write-Host "Or run these commands after creating an empty repo on GitHub:"
Write-Host "  git remote add origin https://github.com/<USERNAME>/<REPO>.git"
Write-Host "  git branch -M main"
Write-Host "  git push -u origin main"

Write-Host "\n3) Deploy to Render"
Write-Host "- Go to https://render.com -> New -> Web Service -> Connect GitHub -> choose the repo -> branch 'main'"
Write-Host "- Set Build Command: bash build.sh"
Write-Host "- Set Start Command: bash start.sh"
Write-Host "- Set Environment variables: SECRET_KEY (and DATABASE_URL if external DB)"

Write-Host "\nDone. If you want I can open a step-by-step or try to use gh to create the repo (if you provide permissions)."