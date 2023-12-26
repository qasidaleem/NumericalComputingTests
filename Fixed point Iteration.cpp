// Qasid Ahmed Aleem
// Fixed Iteration Method
// Date: 29-5-18

#include <stdio.h>
#include <math.h>

// Function declarations
double eqtn_1(double f);
double eqtn_2(double f);
double eqtn_3(double f);

int main() {
    // Initial guesses for roots
    double x1 = 1.5, x2 = 1.5, x3 = 1.5;
    double x_new1 = 0, x_new2 = 0, x_new3 = 0;

    int iterations;
    // User input for the number of iterations
    printf("How many iterations? ");
    scanf("%d", &iterations);

    // Display header for the iteration table
    printf("\tCounter\t\tg1(x)\t\tg2(x)\t\tg3(x)\n");

    // Iterations for finding roots
    for (int i = 0; i < iterations; i++) {
        x_new1 = eqtn_1(x1);
        x_new2 = eqtn_2(x2);
        x_new3 = eqtn_3(x3);

        // Displaying iteration results
        printf("\t%02d\t|%+.16f | %.16f| %.16f|\t\n", i + 1, eqtn_1(x1), eqtn_2(x2), eqtn_3(x3));

        // Updating guesses for the next iteration
        x1 = x_new1;
        x2 = x_new2;
        x3 = x_new3;
    }

    // Displaying the approximate roots
    printf("The approximate roots of g1(x), g2(x), and g3(x) are \n%.16f \n%+.16f \n%+.16f \nrespectively",
           x1, x2, x3);

    return 0;
}

// Equation functions
double eqtn_1(double f) {
    double y = ((10 / f) - 4 * f);
    return pow(y, 0.5); // x = (10/x - 4x)^1/2
}

double eqtn_2(double f) {
    double y = 10 - pow(f, 3);
    return 0.5 * pow(y, 0.5); // 0.5(10 - x^3)^1/2
}

double eqtn_3(double f) {
    double y = 10 / (f + 4);
    return pow(y, 0.5); // x = (10/(x+4))^1.2
}
