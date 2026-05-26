"""Applique le branding schoolsWP au sheet MCP : header dark + vert, zebra, bordures vertes, wrap."""

import json
import subprocess
import sys

SHEET_ID = "1IAYk6TPU1s8W81lfV4r0mEGH_0VyfwsZo53GkuEwe9k"
TAB_ID = 0
LAST_ROW = 44  # 1 header + 43 data rows
LAST_COL = 7

# Palette schoolsWP (reference_brand_colors_schoolswp.md)
DARK = {"red": 15 / 255, "green": 20 / 255, "blue": 25 / 255}  # #0F1419
GREEN = {"red": 0.0, "green": 212 / 255, "blue": 0.0}  # #00D400
LIGHT = {"red": 244 / 255, "green": 245 / 255, "blue": 247 / 255}  # #F4F5F7
WHITE = {"red": 1.0, "green": 1.0, "blue": 1.0}
SOFT_GREY = {"red": 0.85, "green": 0.85, "blue": 0.85}

FULL_RANGE = {
    "sheetId": TAB_ID,
    "startRowIndex": 0,
    "endRowIndex": LAST_ROW,
    "startColumnIndex": 0,
    "endColumnIndex": LAST_COL,
}
HEADER_RANGE = {
    "sheetId": TAB_ID,
    "startRowIndex": 0,
    "endRowIndex": 1,
    "startColumnIndex": 0,
    "endColumnIndex": LAST_COL,
}
BODY_RANGE = {
    "sheetId": TAB_ID,
    "startRowIndex": 1,
    "endRowIndex": LAST_ROW,
    "startColumnIndex": 0,
    "endColumnIndex": LAST_COL,
}

# Col widths : 0=Nom, 1=Source, 2=Transport, 3=Endpoint, 4=Description, 5=Outils, 6=Statut
COL_WIDTHS = [180, 220, 240, 240, 380, 340, 90]

requests = []

# 1. Zebra band : header dark + alternating white/light
requests.append(
    {
        "addBanding": {
            "bandedRange": {
                "range": FULL_RANGE,
                "rowProperties": {
                    "headerColor": DARK,
                    "firstBandColor": WHITE,
                    "secondBandColor": LIGHT,
                },
            }
        }
    }
)

# 2. Header style : dark bg + green bold text centered
requests.append(
    {
        "repeatCell": {
            "range": HEADER_RANGE,
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": DARK,
                    "textFormat": {
                        "foregroundColor": GREEN,
                        "bold": True,
                        "fontSize": 11,
                        "fontFamily": "Inter",
                    },
                    "horizontalAlignment": "CENTER",
                    "verticalAlignment": "MIDDLE",
                    "padding": {"top": 8, "bottom": 8, "left": 8, "right": 8},
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment,verticalAlignment,padding)",
        }
    }
)

# 3. Body style : wrap text + top-aligned + small font + dark fg
requests.append(
    {
        "repeatCell": {
            "range": BODY_RANGE,
            "cell": {
                "userEnteredFormat": {
                    "wrapStrategy": "WRAP",
                    "verticalAlignment": "TOP",
                    "horizontalAlignment": "LEFT",
                    "textFormat": {
                        "fontSize": 10,
                        "fontFamily": "Inter",
                        "foregroundColor": DARK,
                    },
                    "padding": {"top": 6, "bottom": 6, "left": 8, "right": 8},
                }
            },
            "fields": "userEnteredFormat(wrapStrategy,verticalAlignment,horizontalAlignment,textFormat,padding)",
        }
    }
)

# 4. Borders : green outer frame + light grey inner grid
requests.append(
    {
        "updateBorders": {
            "range": FULL_RANGE,
            "top": {"style": "SOLID_MEDIUM", "color": GREEN},
            "bottom": {"style": "SOLID_MEDIUM", "color": GREEN},
            "left": {"style": "SOLID_MEDIUM", "color": GREEN},
            "right": {"style": "SOLID_MEDIUM", "color": GREEN},
            "innerHorizontal": {"style": "SOLID", "color": SOFT_GREY},
            "innerVertical": {"style": "SOLID", "color": SOFT_GREY},
        }
    }
)

# 5. Header row height
requests.append(
    {
        "updateDimensionProperties": {
            "range": {"sheetId": TAB_ID, "dimension": "ROWS", "startIndex": 0, "endIndex": 1},
            "properties": {"pixelSize": 40},
            "fields": "pixelSize",
        }
    }
)

# 6. Column widths
for idx, width in enumerate(COL_WIDTHS):
    requests.append(
        {
            "updateDimensionProperties": {
                "range": {
                    "sheetId": TAB_ID,
                    "dimension": "COLUMNS",
                    "startIndex": idx,
                    "endIndex": idx + 1,
                },
                "properties": {"pixelSize": width},
                "fields": "pixelSize",
            }
        }
    )

# 7. Freeze first column too (nice for scroll)
requests.append(
    {
        "updateSheetProperties": {
            "properties": {
                "sheetId": TAB_ID,
                "gridProperties": {"frozenRowCount": 1, "frozenColumnCount": 1},
            },
            "fields": "gridProperties.frozenRowCount,gridProperties.frozenColumnCount",
        }
    }
)

body = {"requests": requests}

cmd = [
    "gws",
    "sheets",
    "spreadsheets",
    "batchUpdate",
    "--params",
    json.dumps({"spreadsheetId": SHEET_ID}),
    "--json",
    json.dumps(body),
]

res = subprocess.run(cmd, capture_output=True, text=True, shell=True)
print("returncode:", res.returncode)
print("stdout:", res.stdout[:1200])
if res.returncode != 0:
    print("stderr:", res.stderr[:1500], file=sys.stderr)
    sys.exit(res.returncode)
