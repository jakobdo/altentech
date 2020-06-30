import { IExperience } from './Experience';
import { IImage } from './Image';
import { ITechnologyLevel } from './TechnologyLevel';

export interface IConsultant {
    cv: string;
    description: string;
    experience: IExperience[];
    firstname: string;
    fullname: string;
    image: IImage;
    jobtitle: string;
    lastname: string;
    linkedin: string;
    pk: number;
    slug: string;
    tags: number[];
    teaser: string;
    technologyLevels: ITechnologyLevel[];
}