import java.util.Scanner;

public class Month_Printer_20260908 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int month = sc.nextInt();

        // 1~12월 영어 달 이름을 switch 문으로 분기 
        String monthName; // 변수명을 용도에 맞게 수정
        switch (month) {
            case 1:  monthName = "January";   break;
            case 2:  monthName = "February";  break;
            case 3:  monthName = "March";     break;
            case 4:  monthName = "April";     break;
            case 5:  monthName = "May";       break;
            case 6:  monthName = "June";      break;
            case 7:  monthName = "July";      break;
            case 8:  monthName = "August";    break;
            case 9:  monthName = "September"; break;
            case 10: monthName = "October";   break;
            case 11: monthName = "November";  break;
            case 12: monthName = "December";  break;
            default: monthName = "Invalid";   break; // 범위 밖 입력 처리
        }

        // 결과를 출력한다.
        System.out.println(monthName);
        sc.close();
    }
}