@SuppressWarnings("WeakerAccess")
public enum TriangleTypes {
    ORIGINAL, EQUILATERAL, ISOSCELES, NO_TRIANGLE;

    @Override
    public String toString() {
        return switch (TriangleTypes.this) {
            case ORIGINAL -> StringProvider.ORIGINAL_TRIANGLE;
            case EQUILATERAL -> StringProvider.EQUILATERAL_TRIANGLE;
            case ISOSCELES -> StringProvider.ISOSCELES_TRIANGLE;
            case NO_TRIANGLE -> StringProvider.NO_TRIANGLE;
        };
    }
}
