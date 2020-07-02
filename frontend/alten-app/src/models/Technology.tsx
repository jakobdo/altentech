import { IConsultantSimple } from "./Consultant";

export interface ITechnology {
    description: string;
    name: string;
    slug: string;
    consultants: IConsultantSimple[];
}

export interface ITechnologySimple {
    name: string;
    slug: string;
}