@SuppressWarnings("WeakerAccess")
public class CTriangle {
    private double firstSide;
    private double secondSide;
    private double thirdSide;

    private CTriangle() {
        this.firstSide = 0;
        this.secondSide = 0;
        this.thirdSide = 0;
    }

    public static class TriangleCreator {
        private CTriangle instance = null;

        public CTriangle getInstance() {
            if (instance == null) {
                instance = new CTriangle();
            }
            return instance;
        }
    }

    public void setSides(double firstSide, double secondSide, double thirdSide) {
        this.firstSide = firstSide;
        this.secondSide = secondSide;
        this.thirdSide = thirdSide;
    }

    public TriangleTypes getType() throws IllegalArgumentException {
        if (firstSide > 0 && secondSide > 0 && thirdSide > 0) {
            if (firstSide + secondSide <= thirdSide || secondSide + thirdSide <= firstSide || firstSide + thirdSide <= secondSide) {
                return TriangleTypes.NO_TRIANGLE;
            }

            if (firstSide != secondSide && firstSide != thirdSide && secondSide != thirdSide) {
                return TriangleTypes.ORIGINAL;
            } else if (firstSide == secondSide && secondSide == thirdSide) {
                return TriangleTypes.EQUILATERAL;
            } else if (firstSide == secondSide || secondSide == thirdSide) {
                return TriangleTypes.ISOSCELES;
            }

            return TriangleTypes.NO_TRIANGLE;
        } else if (firstSide >= 0 && secondSide >= 0 && thirdSide >= 0) {
            return TriangleTypes.NO_TRIANGLE;
        } else {
            throw new IllegalArgumentException("Invalid shape");
        }
    }
}
