#include <stdlib.h>
#include <stdio.h>
#include <sys/time.h>

int main(int argc, char** argv) {

	int N = 50;

	double** A;
	double** B;
	double** C;

	int i, j, k;

	struct timeval start, end;

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


	gettimeofday(&start, NULL);
	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) {
			C[i][j] = 0.0;
			for (k = 0; k < N; k++)
				C[i][j] += A[i][k] * B[k][j];
		}
	}
	gettimeofday(&end, NULL);

	printf("i-j-k %ld\n", ((end.tv_sec * 1000000 + end.tv_usec)
			- (start.tv_sec * 1000000 + start.tv_usec)));
	
	for (i = 0; i < N; i++)
		for (j = 0; j < N; j++)
			C[i][j] = 0;

	gettimeofday(&start, NULL);
	for (i = 0; i < N; i++) {
		for (k = 0; k < N; k++) {
			C[i][j] = 0.0;
			for (j = 0; j < N; j++)
				C[i][j] += A[i][k] * B[k][j];
		}
	}
	gettimeofday(&end, NULL);

	printf("i-k-j %ld\n", ((end.tv_sec * 1000000 + end.tv_usec)
			- (start.tv_sec * 1000000 + start.tv_usec)));

	for (i = 0; i < N; i++)
		for (j = 0; j < N; j++)
			C[i][j] = 0;

	gettimeofday(&start, NULL);
	for (j = 0; j < N; j++) {
		for (i = 0; i < N; i++) {
			C[i][j] = 0.0;
			for (k = 0; k < N; k++)
				C[i][j] += A[i][k] * B[k][j];
		}
	}
	gettimeofday(&end, NULL);

	printf("j-i-k %ld\n", ((end.tv_sec * 1000000 + end.tv_usec)
			- (start.tv_sec * 1000000 + start.tv_usec)));

	for (i = 0; i < N; i++)
		for (j = 0; j < N; j++)
			C[i][j] = 0;

	gettimeofday(&start, NULL);
	for (j = 0; j < N; j++) {
		for (k = 0; k < N; k++) {
			for (i = 0; i < N; i++)
				C[i][j] += A[i][k] * B[k][j];
		}
	}
	gettimeofday(&end, NULL);

	printf("j-k-i %ld\n", ((end.tv_sec * 1000000 + end.tv_usec)
			- (start.tv_sec * 1000000 + start.tv_usec)));

	for (i = 0; i < N; i++)
		for (j = 0; j < N; j++)
			C[i][j] = 0;

	gettimeofday(&start, NULL);
	for (k = 0; k < N; k++) {
		for (i = 0; i < N; i++) {
			C[i][j] = 0.0;
			for (j = 0; j < N; j++)
				C[i][j] += A[i][k] * B[k][j];
		}
	}
	gettimeofday(&end, NULL);

	printf("k-i-j %ld\n", ((end.tv_sec * 1000000 + end.tv_usec)
			- (start.tv_sec * 1000000 + start.tv_usec)));


	for (i = 0; i < N; i++)
		for (j = 0; j < N; j++)
			C[i][j] = 0;

	gettimeofday(&start, NULL);
	for (k = 0; k < N; k++) {
		for (j = 0; j < N; j++) {
			for (i = 0; i < N; i++)
				C[i][j] += A[i][k] * B[k][j];
		}
	}
	gettimeofday(&end, NULL);

	printf("k-j-i %ld\n", ((end.tv_sec * 1000000 + end.tv_usec)
			- (start.tv_sec * 1000000 + start.tv_usec)));

	free(A);
	free(B);
	free(C);

	free(a);
	free(b);
	free(c);

	return 0;

}
