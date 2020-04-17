#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
 
void BMMultiply(int n, double** a, double** b, double** c)
{
    int bi=0;
    int bj=0;
    int bk=0;
    int i=0;
    int j=0;
    int k=0;
    
    // set block dimension blockSize
    int blockSize=100; 
 
    for(bi=0; bi<n; bi+=blockSize)
        for(bj=0; bj<n; bj+=blockSize)
            for(bk=0; bk<n; bk+=blockSize)
                for(i=0; i<blockSize; i++)
                    for(j=0; j<blockSize; j++)
                        for(k=0; k<blockSize; k++)
                            c[bi+i][bj+j] += a[bi+i][bk+k]*b[bk+k][bj+j];
}
 
int main(void)
{
    int N;
    double** A;
    double** B;
    double** C;
    int numreps = 10;
    int i=0;
    int j=0;
    struct timeval tv1, tv2;
    
    double elapsed = 0.0;
   
    N = 500;
     
    // allocate memory for the matrices
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
	
    // Initialize matrices A & B
    for(i=0; i<N; i++)
    {
        for(j=0; j<N; j++)
        {
            A[i][j] = 1;
            B[i][j] = 2;
        }
    }
 
    // multiply matrices
 
    printf("Multiply matrices %d times...\n", numreps);
    for (i=0; i<numreps; i++)
    {
        gettimeofday(&tv1, NULL);
        BMMultiply(N,A,B,C);
        gettimeofday(&tv2, NULL);
        elapsed += (double) (tv2.tv_sec-tv1.tv_sec) + (double) (tv2.tv_usec-tv1.tv_usec) * 1.e-6;
    }
    printf("Time = %lf \n",elapsed);
 
    // deallocate memory for matrices A, B & C
    free(A);
    free(B);
    free(C);
 
    free(a);
    free(b);
    free(c);   

    return 0;
}
