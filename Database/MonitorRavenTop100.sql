PGDMP     .                    y            raven    13.1 (Debian 13.1-1.pgdg100+1)    13.2     y           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            z           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            {           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            |           1262    16417    raven    DATABASE     Y   CREATE DATABASE raven WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.utf8';
    DROP DATABASE raven;
                postgres    false            ?            1259    16419 	   top100sum    TABLE     ?   CREATE TABLE public.top100sum (
    "time" timestamp with time zone DEFAULT now() NOT NULL,
    "topSum" bigint NOT NULL,
    supply bigint NOT NULL
);
    DROP TABLE public.top100sum;
       public         heap    postgres    false            v          0    16419 	   top100sum 
   TABLE DATA           =   COPY public.top100sum ("time", "topSum", supply) FROM stdin;
    public          postgres    false    200   o       ?
           2606    16425    top100sum top100sum_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.top100sum
    ADD CONSTRAINT top100sum_pkey PRIMARY KEY ("time");
 B   ALTER TABLE ONLY public.top100sum DROP CONSTRAINT top100sum_pkey;
       public            postgres    false    200            v   ?   x?????PE?u~?Q?l?ϵ??? 1,???Z^IW?K?5c???D?K??????B?y3M:???N?d?O??i?"-?? ?:UIQ??w?ѐ??F???qt?t&&????Ѧ?4)?????z??o??1?l?;?     