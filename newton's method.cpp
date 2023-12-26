// Newton's Method
// Qasid Ahmed Aleem
// 24 January 2018

#include<stdio.h>
#include<math.h>



double func_f(double f);
double deri_f(double f);
double x_func(double f);

int main()
{
    double x = 1.5, xn = 0;
    int i, z;
    
    printf("How many iterations do you want (at least 10): ");
    scanf("%d", &z);
    
    printf("\tCounter\tX\t\tf(x)\t\tf'(x)\t\tx'\n");

    for (i = 0; i < z; i += 1)
    {
        xn = x_func(x);
        printf("\t%d\t%.10f\t%.10f\t%.10f\t%.10f\n", i + 1, x, func_f(x), deri_f(x), xn);
        x = xn;
    }

    printf("\nThe approximate root is %.18f", x);
    return 0;
}

double func_f(double f)
{
    return pow(f, 3) + f - 5; // x^3 - x - 5
}

double deri_f(double f)
{
    return 3 * pow(f, 2) + 1; // 3x^2 + 1
}

double x_func(double f)
{
    return f - (func_f(f) / deri_f(f)); // x = x - f(x) / f'(x)
}