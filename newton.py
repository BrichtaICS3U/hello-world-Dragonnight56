def Abs (x) :
	if x < 0 :
		return -x
	elif x > 0 :
		return x
	else :
		return 0

def newton(x, accuracy=0.001) :
  """Compute the square root of the number x using Heron's method. The accuracy is defaulted to three decimal places, but you
  can use a larger or smaller number if you wish. The smaller the number, the more time the calculation will take."""

  Guess = x/2

  while Abs(Guess**2-x) >= accuracy :
    Guess = Guess - ((Guess**2 - x)/(2*Guess))

  return round(Guess,3)
