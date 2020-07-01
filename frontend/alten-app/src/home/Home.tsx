import React, { useEffect, useState } from 'react';

import { Parallax } from 'react-materialize';

import API from './../utils/API';
import { IConsultant } from '../models/Consultant';
import ConsultantFrontpage from '../common/ConsultantFrontpage';
import Loading from './../common/Loading';

function Home() {
    const [consultant, setConsultant] = useState<IConsultant | null>(null);

    useEffect(() => {
        const fetchData = async() => {
            const result = await API.get('/consultants/get_random/');
            setConsultant(result.data);
        };
        fetchData();
    }, []);

    return (
        <div>
            <Parallax
                image={<img alt="" src="https://altentechnology.dk/static/base/gfx/parallax1.jpg"/>}
                options={{
                    responsiveThreshold: 0
                }}
            />
            <div className="section white">
                <div className="row container">
                <h2 className="header">ALTEN Denmark</h2>
                <p className="grey-text text-darken-3 lighten-3">
                    ALTEN Group supports the development strategy of its customers in the fields of innovation, R&D and technological information systems. Created 30 years ago in France, the Group has become a world leader in Engineering and Technology consulting. 34.000 highly qualified engineers carry out studies and conception projects for the Technical and Information Systems Divisions of major customers in the industrial and service sectors. ALTEN DANMARK A/S works within Energy, Life Science, Banking, Insurance and Robot Industries.
                </p>
                </div>
            </div>
            <Parallax
                image={<img alt="" src="https://altentechnology.dk/static/base/gfx/alten.france.jpg"/>}
                options={{
                    responsiveThreshold: 0
                }}
            />
            <div className="section white">
                <div className="row container">
                <h2 className="header">ALTEN Consultant</h2>
                <div className="grey-text text-darken-3 lighten-3">
                {consultant ? (
                    <ConsultantFrontpage consultant={consultant} />
                ) : (
                    <Loading />
                )}
                </div>
                </div>
            </div>
            <Parallax
                image={<img alt="" src="https://altentechnology.dk/static/base/gfx/parallax4.jpg"/>}
                options={{
                    responsiveThreshold: 0
                }}
            />
        </div>
    );
}

export default Home;