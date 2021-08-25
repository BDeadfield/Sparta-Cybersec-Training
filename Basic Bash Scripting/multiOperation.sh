# Get user's numbers for calculations

echo "Enter the first number:  "
read FIRST_NUMBER

echo "Enter the second number:  "
read SECOND_NUMBER

# Set calculation totals
SUM=$((FIRST_NUMBER + SECOND_NUMBER))
SUB=$((FIRST_NUMBER - SECOND_NUMBER))
MUL=$((FIRST_NUMBER * SECOND_NUMBER))

# Store to results.txt

echo $FIRST_NUMBER "+" $SECOND_NUMBER "=" $SUM > results.txt
echo $FIRST_NUMBER "-" $SECOND_NUMBER "=" $SUB >> results.txt
echo $FIRST_NUMBER "*" $SECOND_NUMBER "=" $MUL >> results.txt

# Prevent Division by zero

if [ $FIRST_NUMBER -gt 0 ] && [ $SECOND_NUMBER -gt 0 ]
then
   DIV=$((FIRST_NUMBER / SECOND_NUMBER))
   echo $FIRST_NUMBER "/" $SECOND_NUMBER "=" $DIV >> results.txt
fi

# Display results.txt in console

cat results.txt
