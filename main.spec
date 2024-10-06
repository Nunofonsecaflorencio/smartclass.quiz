# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('assets/logo-no-background.png', 'assets'),
        ('assets/smartclassquiz.ico', 'assets'),
    ],
    hiddenimports=[
        'altgraph', 'annotated_types', 'cachetools', 'certifi', 
        'charset_normalizer', 'colorama', 'google_ai_generativelanguage',
        'google_api_core', 'google_api_python_client', 'google_auth', 
        'google_auth_httplib2', 'google_generativeai', 'googleapis_common_protos', 
        'grpcio', 'grpcio_status', 'grpcio_tools', 'httplib2', 'idna', 
        'ifaddr', 'packaging', 'pefile', 'proto_plus', 'protobuf', 
        'psgcompiler', 'pyasn1', 'pyasn1_modules', 'pydantic', 
        'pydantic_core', 'pyinstaller', 'pyinstaller_hooks_contrib', 
        'pyparsing', 'PySimpleGUI', 'pywin32_ctypes', 'requests', 'rsa',
        'shortuuid', 'tqdm', 'typing_extensions', 'uritemplate', 'urllib3', 
        'zeroconf', 'zeroconf._utils.ipaddress', 'zeroconf._handlers.answers'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='SmartClassQuiz',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=True,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/smartclassquiz.ico'
)
