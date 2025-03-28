public class GreatCircle {
    public static void main(String[] args) {
        if (args.length < 4) {
            System.out.println("Uso: java Assignments.GreatCircle <lat1> <long1> <lat2> <long2>");
            return;
        }

        double x1 = Math.toRadians(Double.parseDouble(args[0]));
        double y1 = Math.toRadians(Double.parseDouble(args[1]));
        double x2 = Math.toRadians(Double.parseDouble(args[2]));
        double y2 = Math.toRadians(Double.parseDouble(args[3]));

        double r = 6371.0;
        double deltaX = (x2 - x1) / 2;
        double deltaY = (y2 - y1) / 2;

        double a = Math.pow(Math.sin(deltaX), 2) +
                Math.cos(x1) * Math.cos(x2) * Math.pow(Math.sin(deltaY), 2);

        double distance = 2 * r * Math.asin(Math.sqrt(a));

        System.out.printf("Distância: %.2f km%n", distance);
    }
}
