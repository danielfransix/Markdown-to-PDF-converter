# Code Examples

This document demonstrates various code formatting options and syntax highlighting capabilities.

## Inline Code

Use `backticks` to create inline code. Examples:

- Variable: `userName`
- Function: `calculateTotal()`
- File path: `/home/user/documents/file.txt`
- Command: `npm install`
- HTML tag: `<div class="container">`

## Basic Code Blocks

### Plain Code Block

```
This is a plain code block
without syntax highlighting.
It preserves formatting and spacing.
```

### Code Block with Language

```text
This is a text code block
with explicit text language specification.
```

## Programming Languages

### Python

```python
# Python example - Data processing
import pandas as pd
import numpy as np
from datetime import datetime

def process_data(filename):
    """
    Process CSV data and return summary statistics.
    
    Args:
        filename (str): Path to the CSV file
    
    Returns:
        dict: Summary statistics
    """
    try:
        # Read the data
        df = pd.read_csv(filename)
        
        # Clean the data
        df = df.dropna()
        df['date'] = pd.to_datetime(df['date'])
        
        # Calculate statistics
        stats = {
            'total_rows': len(df),
            'mean_value': df['value'].mean(),
            'std_value': df['value'].std(),
            'date_range': (df['date'].min(), df['date'].max())
        }
        
        return stats
    
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
        return None
    except Exception as e:
        print(f"Error processing data: {e}")
        return None

# Usage example
if __name__ == "__main__":
    result = process_data('data.csv')
    if result:
        print(f"Processed {result['total_rows']} rows")
        print(f"Mean value: {result['mean_value']:.2f}")
```

### JavaScript

```javascript
// JavaScript example - Async data fetching
class DataService {
    constructor(baseUrl) {
        this.baseUrl = baseUrl;
        this.cache = new Map();
    }

    async fetchUser(userId) {
        // Check cache first
        if (this.cache.has(userId)) {
            return this.cache.get(userId);
        }

        try {
            const response = await fetch(`${this.baseUrl}/users/${userId}`);
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const user = await response.json();
            
            // Cache the result
            this.cache.set(userId, user);
            
            return user;
        } catch (error) {
            console.error('Failed to fetch user:', error);
            throw error;
        }
    }

    async fetchMultipleUsers(userIds) {
        const promises = userIds.map(id => this.fetchUser(id));
        return Promise.all(promises);
    }

    clearCache() {
        this.cache.clear();
    }
}

// Usage
const dataService = new DataService('https://api.example.com');

(async () => {
    try {
        const user = await dataService.fetchUser(123);
        console.log('User:', user.name);
        
        const users = await dataService.fetchMultipleUsers([1, 2, 3]);
        console.log('Users:', users.map(u => u.name));
    } catch (error) {
        console.error('Error:', error.message);
    }
})();
```

### HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsive Card Layout</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header class="header">
        <nav class="navbar">
            <div class="nav-brand">
                <h1>My Website</h1>
            </div>
            <ul class="nav-menu">
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main class="main-content">
        <section class="hero">
            <h2>Welcome to Our Service</h2>
            <p>Discover amazing features and capabilities.</p>
            <button class="cta-button">Get Started</button>
        </section>

        <section class="cards">
            <div class="card">
                <img src="image1.jpg" alt="Feature 1">
                <h3>Feature One</h3>
                <p>Description of the first amazing feature.</p>
            </div>
            <div class="card">
                <img src="image2.jpg" alt="Feature 2">
                <h3>Feature Two</h3>
                <p>Description of the second amazing feature.</p>
            </div>
            <div class="card">
                <img src="image3.jpg" alt="Feature 3">
                <h3>Feature Three</h3>
                <p>Description of the third amazing feature.</p>
            </div>
        </section>
    </main>

    <footer class="footer">
        <p>&copy; 2024 My Website. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

### CSS

```css
/* Modern CSS with Grid and Flexbox */
:root {
    --primary-color: #3498db;
    --secondary-color: #2c3e50;
    --accent-color: #e74c3c;
    --text-color: #333;
    --bg-color: #f8f9fa;
    --border-radius: 8px;
    --box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    color: var(--text-color);
    background-color: var(--bg-color);
}

.header {
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    color: white;
    padding: 1rem 0;
    position: sticky;
    top: 0;
    z-index: 100;
}

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
}

.nav-menu {
    display: flex;
    list-style: none;
    gap: 2rem;
}

.nav-menu a {
    color: white;
    text-decoration: none;
    transition: color 0.3s ease;
}

.nav-menu a:hover {
    color: var(--accent-color);
}

.main-content {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
}

.hero {
    text-align: center;
    padding: 4rem 0;
    background: linear-gradient(45deg, #f0f0f0, #ffffff);
    border-radius: var(--border-radius);
    margin-bottom: 3rem;
}

.cta-button {
    background: var(--primary-color);
    color: white;
    border: none;
    padding: 1rem 2rem;
    border-radius: var(--border-radius);
    font-size: 1.1rem;
    cursor: pointer;
    transition: all 0.3s ease;
}

.cta-button:hover {
    background: var(--secondary-color);
    transform: translateY(-2px);
    box-shadow: var(--box-shadow);
}

.cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.card {
    background: white;
    border-radius: var(--border-radius);
    padding: 1.5rem;
    box-shadow: var(--box-shadow);
    transition: transform 0.3s ease;
}

.card:hover {
    transform: translateY(-5px);
}

.card img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: var(--border-radius);
    margin-bottom: 1rem;
}

@media (max-width: 768px) {
    .navbar {
        flex-direction: column;
        gap: 1rem;
    }
    
    .nav-menu {
        flex-direction: column;
        text-align: center;
    }
    
    .cards {
        grid-template-columns: 1fr;
    }
}
```

### SQL

```sql
-- SQL example - Complex query with CTEs and window functions
WITH monthly_sales AS (
    SELECT 
        DATE_TRUNC('month', order_date) AS month,
        customer_id,
        SUM(total_amount) AS monthly_total,
        COUNT(*) AS order_count
    FROM orders 
    WHERE order_date >= '2023-01-01'
    GROUP BY DATE_TRUNC('month', order_date), customer_id
),
customer_metrics AS (
    SELECT 
        customer_id,
        AVG(monthly_total) AS avg_monthly_spend,
        MAX(monthly_total) AS max_monthly_spend,
        COUNT(DISTINCT month) AS active_months,
        SUM(monthly_total) AS total_spend
    FROM monthly_sales
    GROUP BY customer_id
),
ranked_customers AS (
    SELECT 
        cm.*,
        c.customer_name,
        c.email,
        c.registration_date,
        ROW_NUMBER() OVER (ORDER BY cm.total_spend DESC) AS spend_rank,
        NTILE(5) OVER (ORDER BY cm.total_spend) AS spend_quintile
    FROM customer_metrics cm
    JOIN customers c ON cm.customer_id = c.customer_id
    WHERE cm.active_months >= 3
)
SELECT 
    customer_name,
    email,
    total_spend,
    avg_monthly_spend,
    active_months,
    spend_rank,
    CASE 
        WHEN spend_quintile = 5 THEN 'VIP'
        WHEN spend_quintile = 4 THEN 'Premium'
        WHEN spend_quintile = 3 THEN 'Standard'
        ELSE 'Basic'
    END AS customer_tier,
    ROUND(
        (total_spend / NULLIF(active_months, 0))::numeric, 2
    ) AS avg_monthly_actual
FROM ranked_customers
WHERE spend_rank <= 100
ORDER BY total_spend DESC;

-- Create indexes for performance
CREATE INDEX CONCURRENTLY idx_orders_date_customer 
ON orders (order_date, customer_id);

CREATE INDEX CONCURRENTLY idx_customers_registration 
ON customers (registration_date);
```

### JSON

```json
{
  "name": "markdown-to-pdf-converter",
  "version": "1.0.0",
  "description": "A powerful tool to convert Markdown documents to PDF",
  "main": "main.py",
  "scripts": {
    "start": "python main.py",
    "test": "python test_converter.py",
    "install": "python install_and_test.py"
  },
  "dependencies": {
    "markdown2": "^2.4.10",
    "weasyprint": "^60.0",
    "click": "^8.1.7",
    "colorama": "^0.4.6",
    "Pillow": "^10.0.0"
  },
  "devDependencies": {
    "pytest": "^7.4.0",
    "black": "^23.0.0",
    "flake8": "^6.0.0"
  },
  "keywords": [
    "markdown",
    "pdf",
    "converter",
    "document",
    "python"
  ],
  "author": {
    "name": "Developer",
    "email": "developer@example.com"
  },
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/user/md-to-pdf-converter.git"
  },
  "bugs": {
    "url": "https://github.com/user/md-to-pdf-converter/issues"
  },
  "homepage": "https://github.com/user/md-to-pdf-converter#readme"
}
```

## Command Line Examples

### Bash/Shell

```bash
#!/bin/bash

# Markdown to PDF Converter - Batch processing script

set -euo pipefail  # Exit on error, undefined vars, pipe failures

# Configuration
INPUT_DIR="./markdown_files"
OUTPUT_DIR="./pdf_output"
THEME="default"
LOG_FILE="conversion.log"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Logging function
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Error handling
error_exit() {
    echo -e "${RED}Error: $1${NC}" >&2
    exit 1
}

# Check dependencies
check_dependencies() {
    log "Checking dependencies..."
    
    if ! command -v python3 &> /dev/null; then
        error_exit "Python 3 is required but not installed."
    fi
    
    if ! python3 -c "import markdown2, weasyprint" 2>/dev/null; then
        error_exit "Required Python packages not found. Run: pip install -r requirements.txt"
    fi
    
    log "Dependencies check passed."
}

# Create output directory
setup_directories() {
    log "Setting up directories..."
    
    if [[ ! -d "$INPUT_DIR" ]]; then
        error_exit "Input directory '$INPUT_DIR' does not exist."
    fi
    
    mkdir -p "$OUTPUT_DIR"
    log "Output directory: $OUTPUT_DIR"
}

# Convert single file
convert_file() {
    local input_file="$1"
    local output_file="$2"
    
    log "Converting: $input_file -> $output_file"
    
    if python3 main.py convert "$input_file" --output "$output_file" --theme "$THEME"; then
        echo -e "${GREEN}✓ Successfully converted: $input_file${NC}"
        return 0
    else
        echo -e "${RED}✗ Failed to convert: $input_file${NC}"
        return 1
    fi
}

# Main conversion process
main() {
    log "Starting batch conversion process..."
    
    check_dependencies
    setup_directories
    
    local success_count=0
    local error_count=0
    
    # Find and convert all markdown files
    while IFS= read -r -d '' file; do
        # Get relative path and create output filename
        local rel_path="${file#$INPUT_DIR/}"
        local output_file="$OUTPUT_DIR/${rel_path%.md}.pdf"
        
        # Create output subdirectory if needed
        mkdir -p "$(dirname "$output_file")"
        
        if convert_file "$file" "$output_file"; then
            ((success_count++))
        else
            ((error_count++))
        fi
        
    done < <(find "$INPUT_DIR" -name "*.md" -type f -print0)
    
    # Summary
    log "Conversion completed."
    log "Successful conversions: $success_count"
    log "Failed conversions: $error_count"
    
    if [[ $error_count -eq 0 ]]; then
        echo -e "${GREEN}🎉 All files converted successfully!${NC}"
    else
        echo -e "${YELLOW}⚠️  Some files failed to convert. Check $LOG_FILE for details.${NC}"
    fi
}

# Script entry point
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
```

### PowerShell

```powershell
# PowerShell script for Windows users

param(
    [string]$InputDir = "./markdown_files",
    [string]$OutputDir = "./pdf_output",
    [string]$Theme = "default",
    [switch]$Verbose
)

# Set error action preference
$ErrorActionPreference = "Stop"

# Function to write colored output
function Write-ColorOutput {
    param(
        [string]$Message,
        [string]$Color = "White"
    )
    
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] $Message" -ForegroundColor $Color
}

# Check if Python and required packages are available
function Test-Dependencies {
    Write-ColorOutput "Checking dependencies..." "Yellow"
    
    try {
        $pythonVersion = python --version 2>&1
        Write-ColorOutput "Found: $pythonVersion" "Green"
    }
    catch {
        Write-ColorOutput "Python is not installed or not in PATH" "Red"
        exit 1
    }
    
    try {
        python -c "import markdown2, weasyprint" 2>$null
        Write-ColorOutput "Required packages are available" "Green"
    }
    catch {
        Write-ColorOutput "Required packages missing. Run: pip install -r requirements.txt" "Red"
        exit 1
    }
}

# Main conversion function
function Convert-MarkdownFiles {
    Write-ColorOutput "Starting conversion process..." "Cyan"
    
    # Test dependencies
    Test-Dependencies
    
    # Check input directory
    if (-not (Test-Path $InputDir)) {
        Write-ColorOutput "Input directory '$InputDir' does not exist" "Red"
        exit 1
    }
    
    # Create output directory
    if (-not (Test-Path $OutputDir)) {
        New-Item -ItemType Directory -Path $OutputDir -Force | Out-Null
        Write-ColorOutput "Created output directory: $OutputDir" "Green"
    }
    
    # Find all markdown files
    $markdownFiles = Get-ChildItem -Path $InputDir -Filter "*.md" -Recurse
    
    if ($markdownFiles.Count -eq 0) {
        Write-ColorOutput "No markdown files found in $InputDir" "Yellow"
        return
    }
    
    Write-ColorOutput "Found $($markdownFiles.Count) markdown files" "Cyan"
    
    $successCount = 0
    $errorCount = 0
    
    foreach ($file in $markdownFiles) {
        # Calculate relative path and output filename
        $relativePath = $file.FullName.Substring($InputDir.Length + 1)
        $outputFile = Join-Path $OutputDir ($relativePath -replace '\.md$', '.pdf')
        
        # Create output subdirectory if needed
        $outputDir = Split-Path $outputFile -Parent
        if (-not (Test-Path $outputDir)) {
            New-Item -ItemType Directory -Path $outputDir -Force | Out-Null
        }
        
        try {
            Write-ColorOutput "Converting: $($file.Name)" "White"
            
            $arguments = @(
                "main.py",
                "convert",
                $file.FullName,
                "--output", $outputFile,
                "--theme", $Theme
            )
            
            $process = Start-Process -FilePath "python" -ArgumentList $arguments -Wait -PassThru -NoNewWindow
            
            if ($process.ExitCode -eq 0) {
                Write-ColorOutput "✓ Successfully converted: $($file.Name)" "Green"
                $successCount++
            } else {
                Write-ColorOutput "✗ Failed to convert: $($file.Name)" "Red"
                $errorCount++
            }
        }
        catch {
            Write-ColorOutput "✗ Error converting $($file.Name): $($_.Exception.Message)" "Red"
            $errorCount++
        }
    }
    
    # Summary
    Write-ColorOutput "Conversion completed" "Cyan"
    Write-ColorOutput "Successful: $successCount" "Green"
    Write-ColorOutput "Failed: $errorCount" "Red"
    
    if ($errorCount -eq 0) {
        Write-ColorOutput "🎉 All files converted successfully!" "Green"
    } else {
        Write-ColorOutput "⚠️ Some files failed to convert" "Yellow"
    }
}

# Run the conversion
Convert-MarkdownFiles
```

## Configuration Files

### YAML

```yaml
# Configuration file for the converter
converter:
  default_theme: "default"
  output_format: "pdf"
  
themes:
  default:
    font_family: "Arial, sans-serif"
    font_size: "12pt"
    line_height: 1.6
    margins:
      top: "2cm"
      bottom: "2cm"
      left: "2cm"
      right: "2cm"
    
  academic:
    font_family: "Times New Roman, serif"
    font_size: "11pt"
    line_height: 1.5
    margins:
      top: "2.5cm"
      bottom: "2.5cm"
      left: "3cm"
      right: "2cm"
    
  modern:
    font_family: "Helvetica, Arial, sans-serif"
    font_size: "10pt"
    line_height: 1.4
    margins:
      top: "1.5cm"
      bottom: "1.5cm"
      left: "2cm"
      right: "2cm"

markdown_extensions:
  - "extra"
  - "codehilite"
  - "toc"
  - "tables"
  - "fenced-code"
  - "footnotes"

output_settings:
  include_toc: true
  number_headings: false
  break_on_headings: false
  include_metadata: true
```

## Conclusion

This document demonstrates the comprehensive code formatting capabilities of the Markdown to PDF converter. The converter should preserve syntax highlighting, proper indentation, and code block formatting across all supported languages.

**Key Features Demonstrated**:
- Inline code formatting
- Multi-language syntax highlighting
- Proper indentation preservation
- Line number support (if enabled)
- Code block styling consistency
- Configuration file examples