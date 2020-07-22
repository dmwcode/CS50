#include <cs50.h>
#include <stdio.h>
#include <math.h>

float get_positive_float(void);

int main(void)
{
    float change = get_positive_float();
    int cents = round(change * 100);
    int counter;
    for (counter = 0; cents >= 25; counter+= 1)
    {
        cents = (cents - 25);
    }
    if (cents >= 10)
    for (int i = 0 ; cents >= 10; i+= 1 )
        {
            cents = (cents - 10);
            counter += 1;
        }
    if (cents >= 5)
    {
            cents = (cents - 5);
            counter = counter + 1;
    }
    if (cents >= 1)
    {
        cents = (cents - 5);
        counter = counter + 1;
    } 
    printf("counter = %i\n", counter);
}
float get_positive_float(void)
{
    float n;
    do
    {
        n = get_float("Change owed:  ");
    }
    while (n <= 0);
    printf("n = %f\n", n);
    return n;
}
