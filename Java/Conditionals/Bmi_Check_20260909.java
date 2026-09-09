import java.util.Scanner;

public class Bmi_Check_20260909 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double heightCm = sc.nextDouble();
        double weightKg = sc.nextDouble();

        // cm → m
        double heightM = heightCm / 100;

        // BMI 계산
        double BMI = weightKg / (heightM * heightM);

        String result;

        if (BMI < 18.5) {
            result = "저체중";
        } else if (BMI < 23) {
            result = "정상";
        } else if (BMI < 25) {
            result = "과체중";
        } else {
            result = "비만";
        }

        System.out.printf("BMI: %.2f → %s", BMI, result);
        sc.close();
    }
}