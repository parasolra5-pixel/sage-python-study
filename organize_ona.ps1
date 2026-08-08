# ONA Project Organizer
# Move only - no delete
# Preview first, then ask for approval

$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$memoryBook = Join-Path $root "ONA_MEMORY_BOOK"

if (-not (Test-Path $memoryBook)) {
    Write-Host "ERROR: ONA_MEMORY_BOOK not found." -ForegroundColor Red
    Write-Host "Path: $memoryBook"
    exit 1
}

$moves = @(
    @{ File = "README.md"; Destination = "00_START" }
    @{ File = "ONA_START_PROMPT.md"; Destination = "00_START" }
    @{ File = "ONA_MASTER_HANDOVER.md"; Destination = "00_START" }

    @{ File = "ONA_CONTEXT.md"; Destination = "01_CONTEXT" }
    @{ File = "ONA_PROJECT_CONTEXT.md"; Destination = "01_CONTEXT" }
    @{ File = "ONA_PROJECT_CONTINUATION.md"; Destination = "01_CONTEXT" }
    @{ File = "ONA_STATUS.json"; Destination = "01_CONTEXT" }

    @{ File = "ONA_MEMORY_SYSTEM_v2.0.md"; Destination = "02_DESIGN" }

    @{ File = "ONA_MEMORY_BOOK.md"; Destination = "04_HISTORY" }
    @{ File = "ONA_TIMELINE.md"; Destination = "04_HISTORY" }

    @{ File = "ONA_HANDOVER.md"; Destination = "05_HANDOVER" }
    @{ File = "ONA_HANDOVER_SUMMARY.md"; Destination = "05_HANDOVER" }
)

Write-Host ""
Write-Host "======================================"
Write-Host " ONA PROJECT ORGANIZER - PREVIEW"
Write-Host "======================================"
Write-Host ""

$validMoves = @()

foreach ($move in $moves) {

    $source = Join-Path $memoryBook $move.File
    $destinationFolder = Join-Path $memoryBook $move.Destination
    $destination = Join-Path $destinationFolder $move.File

    if (Test-Path $source) {

        if (Test-Path $destination) {

            Write-Host "[SKIP] Destination already exists:" -ForegroundColor Yellow
            Write-Host "       $($move.File)"
            Write-Host "       -> $($move.Destination)"
            Write-Host ""

        }
        else {

            Write-Host "[MOVE]"
            Write-Host "       $($move.File)"
            Write-Host "       -> $($move.Destination)"
            Write-Host ""

            $validMoves += @{
                Source = $source
                DestinationFolder = $destinationFolder
                Destination = $destination
                File = $move.File
            }
        }
    }
}

Write-Host "--------------------------------------"
Write-Host "Files ready to move: $($validMoves.Count)"
Write-Host "Files will NOT be deleted."
Write-Host "--------------------------------------"
Write-Host ""

$answer = Read-Host "Proceed with these moves? (Y/N)"

if ($answer -notmatch "^[Yy]$") {

    Write-Host ""
    Write-Host "CANCELLED. No files were changed." -ForegroundColor Yellow
    exit 0
}

Write-Host ""
Write-Host "Starting file moves..." -ForegroundColor Green
Write-Host ""

foreach ($item in $validMoves) {

    if (-not (Test-Path $item.DestinationFolder)) {
        New-Item -ItemType Directory -Path $item.DestinationFolder -Force | Out-Null
    }

    Move-Item `
        -Path $item.Source `
        -Destination $item.Destination

    Write-Host "[OK] $($item.File) -> $($item.DestinationFolder)" `
        -ForegroundColor Green
}

Write-Host ""
Write-Host "======================================"
Write-Host " ONA ORGANIZATION COMPLETE"
Write-Host "======================================"
Write-Host ""
Write-Host "Moved: $($validMoves.Count)"
Write-Host "Deleted: 0"
Write-Host ""