async function predictPrice() {


    const button =
        document.getElementById("predictButton");


    const result =
        document.getElementById("result");


    const price =
        document.getElementById("price");


    const error =
        document.getElementById("error");


    const loading =
        document.getElementById("loading");


    // Previous result hide karo

    result.style.display = "none";

    error.style.display = "none";


    // Data collect karo

    const data = {

        AccelSec:
            Number(
                document.getElementById("AccelSec").value
            ),

        TopSpeed_KmH:
            Number(
                document.getElementById("TopSpeed_KmH").value
            ),

        Range_Km:
            Number(
                document.getElementById("Range_Km").value
            ),

        Efficiency_WhKm:
            Number(
                document.getElementById("Efficiency_WhKm").value
            ),

        FastCharge_KmH:
            Number(
                document.getElementById("FastCharge_KmH").value
            ),

        Seats:
            Number(
                document.getElementById("Seats").value
            ),

        RapidCharge:
            document.getElementById("RapidCharge").value,

        PowerTrain:
            document.getElementById("PowerTrain").value,

        PlugType:
            document.getElementById("PlugType").value,

        BodyStyle:
            document.getElementById("BodyStyle").value,

        Segment:
            document.getElementById("Segment").value
    };


    // Check numeric fields

    if (

        !data.AccelSec ||

        !data.TopSpeed_KmH ||

        !data.Range_Km ||

        !data.Efficiency_WhKm ||

        !data.FastCharge_KmH ||

        !data.Seats

    ) {

        error.innerText =
            "Please fill all numeric fields.";

        error.style.display = "block";

        return;
    }


    // Button disable

    button.disabled = true;

    button.innerText = "Predicting...";


    loading.style.display = "block";


    try {


        // Flask API ko request

        const response = await fetch(
            "/predict",
            {

                method: "POST",

                headers: {

                    "Content-Type":
                        "application/json"

                },

                body:
                    JSON.stringify(data)

            }
        );


        // Response check

        if (!response.ok) {

            throw new Error(
                "Server error"
            );

        }


        const prediction =
            await response.json();


        // Price show karo

        price.innerText =
            "€" +
            Number(
                prediction.predicted_price
            ).toLocaleString("en-IN");


        result.style.display = "block";


    }

    catch (err) {


        console.error(err);


        error.innerText =
            "Prediction failed. Please check Flask server.";


        error.style.display =
            "block";

    }


    finally {


        loading.style.display =
            "none";


        button.disabled =
            false;


        button.innerText =
            "Predict Car Price";

    }

}