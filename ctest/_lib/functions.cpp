double addNumbers (double a, double b) {
    double sum;
    sum = a+b;
    return sum;
}

void lennardJonesPotential(double *target, double r[], double eps, double sig) {
    double r2, r6i, result;
    int count;
    count = sizeof(r) / sizeof(r[0]);
    for (int i=0; i<count; ++i) {
        r2 = sig * sig * r[i] * r[i];
        r6i = 1/(r2 * r2 * r2);
        result = (4 * eps) * (r6i*r6i - r6i);
        target[i] = result;
    }
}