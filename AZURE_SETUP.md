# Azure Blob Storage Setup for Images

## Step 1: Create a Storage Account in Azure

1. Go to [Azure Portal](https://portal.azure.com)
2. Click **"+ Create a resource"**
3. Search for **"Storage account"** and click it
4. Click **"Create"**

### Fill in the form:
- **Resource Group**: Select your existing resource group (same one as your app)
- **Storage account name**: `djangostorageXXXX` (lowercase, 3-24 chars, globally unique)
  - Example: `djangostorage12345`
- **Region**: Same as your App Service (Canada Central)
- **Performance**: Standard
- **Redundancy**: Locally-redundant storage (LRS)
- Click **"Review + create"** → **"Create"**

## Step 2: Create a Container for Media Files

1. Once created, go to your Storage Account
2. Click **"Containers"** in the left menu
3. Click **"+ Container"**
4. Name: `media`
5. Public access level: **Blob** (to allow public image viewing)
6. Click **"Create"**

## Step 3: Get Your Storage Keys

1. In your Storage Account, go to **"Access keys"** in left menu
2. Copy these two values:
   - **Storage account name** (top of page)
   - **Key1** (under "key1" - copy the full key string)

## Step 4: Add Environment Variables to Azure App Service

1. Go to your **App Service** in Azure Portal
2. Click **"Configuration"** in left menu
3. Click **"+ New application setting"** for each:

| Name | Value |
|------|-------|
| `AZURE_STORAGE_ACCOUNT_NAME` | Your storage account name (e.g., `djangostorage12345`) |
| `AZURE_STORAGE_ACCOUNT_KEY` | Your Key1 value (the long string) |

4. Click **"Save"** at the top
5. The app will restart automatically

## Step 5: Deploy Your Code

```bash
git add .
git commit -m "Add Azure Blob Storage for image uploads"
git push
```

Azure will auto-deploy and run migrations.

## Step 6: Test Image Upload

### Via Postman:
- **POST** `https://your-app-name.azurewebsites.net/api/products/`
- **Body** → **form-data**:
  - Key: `name` → Value: `Laptop`
  - Key: `price` → Value: `999.99`
  - Key: `image` → Select FILE

### Via Django Admin:
1. Go to `https://your-app-name.azurewebsites.net/admin/`
2. Login
3. Click "Products" → "Add Product"
4. Upload image and save

**Images will now be stored in Azure Blob Storage!** ✅

## Troubleshooting

### Getting "Access Denied" errors?
- Double-check your storage account name and key in Application Settings
- Make sure the `media` container exists and is set to "Blob" access level

### Container not created?
- Manually create it via Azure Portal → Storage Account → Containers → + Container

### Images not showing?
- Check the image URL in your API response
- It should start with `https://youraccountname.blob.core.windows.net/media/...`
