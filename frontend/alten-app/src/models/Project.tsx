import { IConsultantSimple } from "./Consultant";
import { ITechnologySimple } from "./Technology";

export interface IProject {
    name: string;
    slug: string;
    description: string;
    client: number | null;
    industry: string | null;
    technologies: ITechnologySimple[];
    consultants: IConsultantSimple[];
}

export interface IProjectSimple {
    name: string;
    slug: string;
    technologies: ITechnologySimple[];
}