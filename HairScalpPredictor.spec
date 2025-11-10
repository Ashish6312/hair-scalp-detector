# -*- mode: python ; coding: utf-8 -*-
import os
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

block_cipher = None

# Get the current directory
spec_root = os.path.abspath(SPECPATH)

# Collect all Django files
django_datas = [
    (os.path.join(spec_root, 'minor', 'myapp', 'templates'), os.path.join('minor', 'myapp', 'templates')),
    (os.path.join(spec_root, 'minor', 'myapp', 'migrations'), os.path.join('minor', 'myapp', 'migrations')),
    (os.path.join(spec_root, 'minor', 'minor'), os.path.join('minor', 'minor')),
    (os.path.join(spec_root, 'minor', 'manage.py'), 'minor'),
    (os.path.join(spec_root, 'best_model.pth'), '.'),
]

# Add db.sqlite3 if it exists
db_path = os.path.join(spec_root, 'minor', 'db.sqlite3')
if os.path.exists(db_path):
    django_datas.append((db_path, 'minor'))

# Collect Django templates and static files
try:
    django_datas += collect_data_files('django.contrib.admin')
    django_datas += collect_data_files('django.contrib.auth')
except:
    pass

# Collect all required Python packages
hiddenimports = [
    'django',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.template.loaders.filesystem',
    'django.template.loaders.app_directories',
    'torch',
    'torchvision',
    'torchvision.models',
    'torchvision.transforms',
    'PIL',
    'PIL.Image',
    'numpy',
]

# Add all Django submodules
try:
    hiddenimports += collect_submodules('django')
except:
    pass

a = Analysis(
    [os.path.join(spec_root, 'run_app.py')],
    pathex=[spec_root],
    binaries=[],
    datas=django_datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['matplotlib', 'scipy', 'pandas', 'tensorflow'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='HairScalpDiseasePredictor',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='HairScalpDiseasePredictor',
)
