--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: huaweiphone; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.huaweiphone (
    nama_produk text,
    layar text,
    prosesor text,
    ram integer,
    penyimpanan integer,
    kamera_belakang integer,
    kamera_depan integer,
    baterai integer,
    harga bigint
);


ALTER TABLE public.huaweiphone OWNER TO postgres;

--
-- Data for Name: huaweiphone; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.huaweiphone (nama_produk, layar, prosesor, ram, penyimpanan, kamera_belakang, kamera_depan, baterai, harga) FROM stdin;
Huawei Y5p	5.45 inci	MediaTek MT6762R 2.0 GHz	2	32	8	5	3020	1499000
Huawei Y6p	6.3 inci	MediaTek MT6762R 2.0 GHz	3	64	13	8	5000	1999000
Huawei Y7p	6.39 inci	HiSilicon Kirin 710F 2.2 GHz	4	64	48	8	4000	2499000
Huawei Y8p	6.3 inci	HiSilicon Kirin 710F 2.2 GHz	6	128	48	16	4000	3499000
Huawei Y9s	6.59 inci	HiSilicon Kirin 710F 2.2 GHz	6	128	48	16	4000	3999000
Huawei P40 Lite E	6.39 inci	HiSilicon Kirin 710F 2.2 GHz	4	64	48	8	4000	2799000
Huawei P Smart 2021	6.67 inci	HiSilicon Kirin 710A 2.0 GHz	4	128	48	8	5000	3299000
Huawei Nova 7i	6.4 inci	HiSilicon Kirin 810 2.27 GHz	8	128	48	16	4200	4999000
Huawei Enjoy 10e	6.3 inci	MediaTek Helio P35 2.3 GHz	4	64	13	8	5000	2299000
Huawei Mate 30 Lite	6.26 inci	HiSilicon Kirin 810 2.27 GHz	6	128	48	24	4000	5999000
\.


--
-- PostgreSQL database dump complete
--

