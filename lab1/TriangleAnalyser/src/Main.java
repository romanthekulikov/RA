public class Main {
    public static void main(String[] args) {
        try {
            if (args.length > 3) {
                throw new IllegalArgumentException("Too much");
            }
            double firstSide = Double.parseDouble(args[0]);
            double secondSide = Double.parseDouble(args[1]);
            double thirdSide = Double.parseDouble(args[2]);
            CTriangle triangle = new CTriangle.TriangleCreator().getInstance();
            triangle.setSides(firstSide, secondSide, thirdSide);
            String triangleType = triangle.getType().toString();
            System.out.println(triangleType);
        } catch (Exception exception) {
            String errorMessage = StringProvider.ERROR;
            System.out.println(errorMessage);
        }
    }
}