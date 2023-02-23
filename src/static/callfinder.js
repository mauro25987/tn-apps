const sources = document.getElementById("sources");
const campaigns = document.getElementById("campaigns");

const getCampaigns = () => {
    while(campaigns.options.length > 0) {
        campaigns.remove(0)    
    }
    axios.get(SCRIPT_ROOT + SCRIPT_ROOT + "api/_get_campaigns/" + sources.value)
        .then( response  => {
            response.data.map(elem => {
                let option = document.createElement("option");
                option.value = elem;
                option.text = elem;
                campaigns.appendChild(option);
            }); 
        });
}

const getSources = () => {
    axios.get(SCRIPT_ROOT + "api/_get_sources")
        .then( response => {
            response.data.map(elem => {
                let option = document.createElement("option");
                option.value = elem;
                option.text = elem;
                sources.appendChild(option);
            });
            sources.options[0].selected = true;
        });
}

document.addEventListener("DOMContentLoaded", () => {
    getSources();
    sources.addEventListener("change", getCampaigns);
});
