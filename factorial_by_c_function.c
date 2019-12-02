//definning factorial function using c language
long factorial(int x)
{
  long i,y=1;
  if (x<0)
    {
      return -1;
    }
  else
    {
     for (i=0;i<x;i++)
      {
      y=y*(i+1);
      }
     return y;
    }
}
  int main()
  {
    return 0;
  }

