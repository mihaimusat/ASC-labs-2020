#include <stdlib.h>
#include <stdio.h>
#include <sys/time.h> 

int main(int argc, char** argv) {

	int N = 100;

	int i, j, k, p;

	p = atoi(argv[1]);

	struct timeval start, end;

	double** A;
	double** B;
	double** C;

	double* a = malloc(N * N * sizeof(double));
    	if(a == NULL) {
		printf("malloc failed\n");
		exit(-2);
    	}

	A = malloc(N * sizeof(double**));
	for(i = 0; i < N; i++) {
		A[i] = &a[N * i];
	}

	
	double* b = malloc(N * N * sizeof(double));
    	if(b == NULL) {
		printf("malloc failed\n");
		exit(-2);
    	}

	B = malloc(N * sizeof(double**));
	for(i = 0; i < N; i++) {
		B[i] = &b[N * i];
	}

	double* c = malloc(N * N * sizeof(double));
    	if(c == NULL) {
		printf("malloc failed\n");
		exit(-2);
    	}

	C = malloc(N * sizeof(double**));
	for(i = 0; i < N; i++) {
		C[i] = &c[N * i];
	}

	for (i = 0; i < N; i++)
		for (j = 0; j < N; j++) {
			A[i][j] = 1;
			B[i][j] = 2;
		}

	if (p != 0)
		goto pointer;


	// optimizare folosind constanta
 
	gettimeofday(&start, NULL); 
 
	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) {
			register double suma = 0.0;
			for (k = 0; k < N; k++)
				suma += A[i][k] * B[k][j];
			C[i][j] = suma;
		}
	}

	gettimeofday(&end, NULL);

	printf("Time = %ld\n", ((end.tv_sec * 1000000 + end.tv_usec)
			- (start.tv_sec * 1000000 + start.tv_usec)));

	free(A);
	free(B);
	free(C);

	free(a);
	free(b);
	free(c);

	return 0;

	pointer:

	// optimizare acces la vectori

	gettimeofday(&start, NULL);

	for (i = 0; i < N; i++) {
	  
		double *orig_pa = &A[i][0];
		for(j = 0; j < N; j++) {
			double *pa = orig_pa;
			double *pb = &B[0][j];
			register double suma = 0;
			for (k = 0; k < N; k++) {
				suma += *pa * *pb;
				pa++;
				pb += N;
			}
			C[i][j] = suma;
		}
	}

	gettimeofday(&end, NULL);

	printf("Time = %ld\n", ((end.tv_sec * 1000000 + end.tv_usec)
			- (start.tv_sec * 1000000 + start.tv_usec)));

	free(A);
	free(B);
	free(C);

	free(a);
	free(b);
	free(c);


	return 0;

}
