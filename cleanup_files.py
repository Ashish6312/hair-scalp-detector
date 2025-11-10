"""
Clean up unnecessary documentation files
"""
import os

# Files to delete (non-essential documentation)
files_to_delete = [
    "CAMERA_FIXES_SUMMARY.md",
    "🔧_FIX_APPLIED.txt",
    "🎯_YOUR_DEPLOYMENT_STEPS.txt",
    "✅_DEPLOYMENT_PROGRESS.txt",
    "⚡_DEPLOY_NOW.txt",
    "DEPLOY_CHECKLIST.txt",
    "DEPLOYMENT_ARCHITECTURE.txt",
    "🎉_READY_TO_DEPLOY.txt",
    "✅_FOOTER_UPDATED.txt",
    "camera_capture_fix.js",
    "PROFESSIONAL_DESIGN_SUMMARY.md",
    "HEAD_MASK_DETECTION_GUIDE.md",
    "update_footers.py",  # This script itself after running
]

def main():
    print("=" * 70)
    print("Cleaning Up Non-Essential Files")
    print("=" * 70)
    print()
    
    deleted_count = 0
    
    for filename in files_to_delete:
        if os.path.exists(filename):
            try:
                os.remove(filename)
                print(f"✓ Deleted: {filename}")
                deleted_count += 1
            except Exception as e:
                print(f"✗ Error deleting {filename}: {e}")
        else:
            print(f"- Not found: {filename}")
    
    print()
    print("=" * 70)
    print(f"✅ Deleted {deleted_count} files")
    print("=" * 70)
    print()
    print("Keeping essential files:")
    print("  - README.md")
    print("  - DEPLOYMENT_GUIDE.md")
    print("  - 📱_MOBILE_APP_GUIDE.md")
    print("  - 📱_MOBILE_APP_SUMMARY.txt")
    print("  - 🎉_DEPLOYMENT_SUCCESS.txt")
    print()

if __name__ == '__main__':
    main()
