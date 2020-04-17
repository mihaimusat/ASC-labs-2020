#include <malloc.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include <sys/time.h>


int main(int argc, char* argv[])
{
    if(argc != 4)
    {
        printf("apelati cu %s <line_size> <vector_size> <iterations>\n", argv[0]);
        return -1;
    }

    int64_t l = atoi(argv[1]);  // dimensiunea liniei de cache
    int64_t n = atoi(argv[2]);  // dimensiunea vectorului
    int64_t c = atoi(argv[3]);  // numarul de iteratii

    // TODO alocari si initializari
    char* x = calloc(n, sizeof(char));
    if(x == NULL) {
        printf("calloc failed\n");
        exit(-2);
    }

    struct timeval start, end;
    gettimeofday(&start, NULL);

    // TODO bucla de test
    // in variabila ops calculati numarul de operatii efectuate
	
    for(int64_t step = 0; step < c; step++) {
    	for(int64_t i = 0; i < n; i += l) {
        	x[i]++;
	}
    }
    int64_t ops = (n/l) * c;

    gettimeofday(&end, NULL);

    float elapsed = ((end.tv_sec - start.tv_sec)*1000000.0f + end.tv_usec - start.tv_usec)/1000000.0f;
    printf("%12ld, %12ld, %12f, %12g\n", n, ops, elapsed, ops/elapsed);

    free(x);

    return 0;
}

