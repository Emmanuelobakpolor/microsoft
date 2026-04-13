# Azure Deployment - Final Setup Steps

Your code is pushed! Now follow these steps to make it work:

## Step 1: Set Startup Command in Azure Portal

1. Go to [Azure Portal](https://portal.azure.com)
2. Find your App Service: `emmanuel-django-test-123`
3. Click **"Configuration"** in the left menu
4. Click **"General settings"** tab
5. In the **"Startup Command"** field, enter:
   ```
   /home/site/wwwroot/startup.sh
   ```
6. Click **"Save"** at the top
7. Your app will restart automatically

## Step 2: Restart the App (if needed)

If it doesn't auto-restart:
1. Go to Overview page
2. Click **"Restart"** button
3. Wait 30 seconds for it to come back online

## Step 3: Test Your API

Your app should now be working!

Test with Postman:
- **GET**: `https://emmanuel-django-test-123-c4bjh0hacjgfb2ar.canadacentral-01.azurewebsites.net/api/products/`
- Should return: `{"products": [], "count": 0}`

## Step 4: Create a Superuser (Optional)

To access the admin panel, create a superuser:

In Azure Portal → App Service → SSH:
```bash
python manage.py createsuperuser
```

Then go to:
```
https://your-app-name.azurewebsites.net/admin/
```

---

## Troubleshooting

**Still getting errors?**
- Go to Deployment Center to check build logs
- Check Log Stream (under Monitoring) for real-time errors
- Make sure `startup.sh` is executable

**Getting "ModuleNotFoundError"?**
- Verify the startup command is set correctly
- Check that requirements.txt includes all packages
