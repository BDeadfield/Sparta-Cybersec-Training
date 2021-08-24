# Get current directory path
$SCRIPT_PATH = Split-Path -parent $MyInvocation.MyCommand.Definition

# Get user's numbers for calculations
[int]$FIRST_NUM = Read-Host "Please enter the first number:  "
[int]$SECOND_NUM = Read-Host "Please enter the second number:  "

# Set calculation totals
$SUM = $FIRST_NUM + $SECOND_NUM
$SUB = $FIRST_NUM - $SECOND_NUM
$MUL = $FIRST_NUM * $SECOND_NUM

# Display calculations and save to results text file
Write-Output "$FIRST_NUM + $SECOND_NUM = $SUM" | tee -a $SCRIPT_PATH\results.txt
Write-Output "$FIRST_NUM - $SECOND_NUM = $SUB" | tee -a $SCRIPT_PATH\results.txt
Write-Output "$FIRST_NUM * $SECOND_NUM = $MUL" | tee -a $SCRIPT_PATH\results.txt

# Prevent division if any of the numbers equals zero
if ($FIRST_NUM -and $SECOND_NUM -gt 0)
{
  $DIV = $FIRST_NUM / $SECOND_NUM
  Write-Output "$FIRST_NUM / $SECOND_NUM = $DIV" | tee -a $SCRIPT_PATH\results.txt
}
