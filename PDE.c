#include <stdio.h>
main(){
  float E = 100.0;
  float A = 1.0;
  float L = 10.0;
  int n_cells = 30;
  int n_nodes = n_cells+1;
  float mesh[n_nodes];
  float h = L/n_cells;
  for (int i=0 ; i<n_nodes ; i++){
    mesh[i] = i*h
}
  printf(mesh);
}

float distributed_load(float x){
  return 1.0;
}
