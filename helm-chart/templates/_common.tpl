{{- define "pullSecret" -}}
imagePullSecrets:
  - name: {{ .Values.imagePullSecret }}
  - name: regcred
{{- end -}}


{{- define "prometheusAnnotation" -}}
{{- if .Values.prometheus }}
prometheus.io/scrape: 'true'
prometheus.io/path: '{{ .Values.prometheus.path }}'
prometheus.io/port: '{{ .Values.prometheus.port }}'
{{- end -}}
{{- end -}}

{{- define "commonEnv" -}}
- name: DEBUG_LOG
  value: '{{ .Values.debug }}'
- name: CORS_ORIGINS
  value: '{{ toJson .Values.cors }}'
{{- end -}}
