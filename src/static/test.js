const sources = document.getElementById("sources");
const campaigns = document.getElementById("campaigns");
const agents = document.getElementById("agents");
const types = document.getElementById("types");
const ingroups = document.getElementById("ingroups");
const dispos = document.getElementById("dispos");

const getSources = () => {
    axios.get(SCRIPT_ROOT + "api/_get_sources")
        .then( response => {
            response.data.map(elem => {
                let option = document.createElement("option");
                option.value = elem;
                option.text = elem;
                sources.appendChild(option);
            });
        });
}

const getCampaigns = () => {
    while(campaigns.options.length > 0) {
        campaigns.remove(0)    
    }
    axios.get(SCRIPT_ROOT + "api/_get_campaigns/" + sources.value)
        .then( response  => {
            response.data.map(elem => {
                let option = document.createElement("option");
                option.value = elem[0];
                option.text = elem[1];
                campaigns.appendChild(option);
            }); 
        });
}

const getAgentsByCampaing = () => {
    while(agents.options.length > 0) {
        agents.remove(0)
    }
    axios.get(SCRIPT_ROOT + "api/_get_agents_by_campaign/" + sources.value + "/" + campaigns.value)
        .then( response  => {
            response.data.map(elem => {
                let option = document.createElement("option");
                option.value = elem[0];
                option.text = elem[0] + " " + elem[1];
                agents.appendChild(option);
            }); 
        });
}

const getTypes = () => {
    axios.get(SCRIPT_ROOT + "api/_get_types")
        .then( response => {
            for(elem in response.data){
                let option = document.createElement("option");
                option.value = elem;
                option.text = response.data[elem]
                types.appendChild(option);
            };           
        });
}

const getCampaignsByType = () => {
    while(campaigns.options.length > 0) {
        campaigns.remove(0)    
    }
    axios.get(SCRIPT_ROOT + "api/_get_campaigns_by_type/" + sources.value + "/" + types.value)
        .then( response  => {
            response.data.map(elem => {
                let option = document.createElement("option");
                option.value = elem[0];
                option.text = elem[1];
                campaigns.appendChild(option);
            }); 
        });
}

const getIngroupsByCampaign = () => {
    while(ingroups.options.length > 0) {
        ingroups.remove(0)
    }
    axios.get(SCRIPT_ROOT + "api/_get_ingroups_by_campaign/" + sources.value + "/" + campaigns.value)
        .then( response => {
            response.data.map(elem => {
                let option = document.createElement("option");
                option.value = elem[0];
                option.text = elem[1];
                ingroups.appendChild(option);
            });
        });
}

const getDisposByCampaign = () => {
    while(dispos.options.length > 0) {
        dispos.remove(0)
    }
    axios.get(SCRIPT_ROOT + "api/_get_dispos_by_campaign/" + sources.value + "/" + campaigns.value)
        .then( response => {
            response.data.map(elem => {
                let option = document.createElement("option");
                option.value = elem[0];
                option.text = elem[1];
                dispos.appendChild(option);
            });
        });
}

window.addEventListener("DOMContentLoaded", () => {
    getSources();
});

sources.addEventListener("change", () => {
    getCampaigns();
    getTypes();
});

campaigns.addEventListener("change", () => {
    getAgentsByCampaing();
    getIngroupsByCampaign();
    getDisposByCampaign();
});

types.addEventListener("change", () => {
    getCampaignsByType();
});